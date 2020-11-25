class Term:
    '''
    Term type. Term can be either one of these form:
    -   const  or  Variable  or  _variable
    -   function(...)
    '''
    def __init__(self, string = ""):
        brk = string.find("(")
        if brk != -1:
            self.op = string[:brk]
            self.args = string[brk+1:-1].split(",")
            self.args = [Term(x) for x in self.args]
        else:
            self.op = string
            self.args = None


    def __eq__(self, other):
        if type(other) != Term:
            return False
        return self.op == other.op and self.args == other.args


    def __repr__(self):
        res = self.op
        if self.args is not None:
            res = res + "(" + ", ".join([repr(x) for x in self.args]) + ")"
        return res


    def __hash__(self):
        return hash(repr(self))

        
    @property
    def type_t(self):
        if self.args is not None:
            return "function"
        elif self.op[0] == "_" or self.op[0].isupper():
            return "variable"
        else:
            return "constant"

    
    @property
    def var_list(self):
        if self.type_t == "variable":
            return [self.op]
        elif self.type_t == "function":
            res = []
            for t in self.args:
                res += t.var_list
            res = list(dict.fromkeys(res))  #Remove duplicate variable
            return res
        else:
            return []


    def sub(self, theta):
        if self.type_t == "variable" and self.op in theta:
            res = theta[self.op]
            while not res.sub(theta) == res:
                res = res.sub(theta)
            return res
        elif self.type_t == "function":
            res = Term()
            res.op = self.op
            res.args = [t.sub(theta) for t in self.args]
            return res
        else:
            return self



class Predicate(Term):
    '''
    Predicate type. Predicate can be either one of these forms:
    -   Relate: name  or  name(term, term,...)
    -   Negate: not(name(...))
    -   Unify:  term = term or term \\= term
    '''
    def __init__(self, string = ""):    
        # Parse not
        if string.startswith("not("):
            string = string[4:-1]   # Strip not(...)
            self.truth = False
        else:
            self.truth = True

        # Parse = and \=
        if "=" in string:
            # Parse \
            if "\\" in string:
                self.truth = False
                string = string.replace("\\", "")

            # Convert "=" operator to "=" relation
            string = string.replace("=", ",")
            string = "=(" + string + ")"

        # Predicate is just a function return truth instead of obj
        # So parse the rest just like a term
        super().__init__(string)
    

    def __eq__(self, other):
        if type(other) != Predicate:
            return False
        return self.op == other.op and self.args == other.args and self.truth == other.truth


    def __hash__(self):
        return hash(repr(self))


    @property
    def type_t(self):
        return "predicate"


    @property
    def var_list(self):
        res = []
        for t in self.args:
            res += t.var_list
        res = list(dict.fromkeys(res))  # Remove duplicate variable
        return res


    def sub(self, theta):
        res = Predicate()
        res.truth = self.truth
        res.op = self.op
        res.args = [t.sub(theta) for t in self.args]
        return res


    def neg(self):
        res = Predicate()
        res.truth = not self.truth
        res.op = self.op
        res.args = self.args
        return res


    def standardize(self, args):
        if type(args) != set:
            raise TypeError("standardize only accept set of strings.")

        trans = {}

        for var in self.var_list:
            if var in args:
                new_var = var
                while new_var in args:
                    new_var = new_var + "%"
                trans[var] = Term(new_var)

        return self.sub(trans)