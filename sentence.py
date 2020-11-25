from term import *
from utility import list_contain, algebra_split
from string import whitespace

class Sentence:
    '''
    Sentence type. Sentence can be either one of these forms:
    -   Fact:   Predicate :- None
    -   Rule:   Predicate :- Predicate
    -   Query:  None :- Predicate
    '''

    def __init__(self, string = None, is_query = False):
        if string is None:
            self.inference = []
            self.premise = []
        else:
            # Remove every whitespace from string
            string = string.translate({ord(c): None for c in whitespace})

            # Break down a string into 2 parts: inference and premise
            string = string.split(":-")

            # Parse inference part
            preds = algebra_split(string[0])
            self.inference = [Predicate(p) for p in preds]

            # Parse premise part
            if len(string) > 1:
                preds = algebra_split(string[1])
                self.premise = [Predicate(p) for p in preds]
            else:
                self.premise = []

            # If this string is a query then swap predicate to premise
            if is_query:
                self.premise, self.inference = self.inference, self.premise
                if len(string) > 1:
                    # Query does not accept :-
                    raise TypeError


    def __eq__(self, other):
        if type(other) != Sentence:
            return False
        return list_contain(self.premise, other.premise) and list_contain(self.inference, other.inference)


    def __add__(self, other):
        res = Sentence()
        res.inference = self.inference + other.inference
        res.premise = self.premise + other.premise
        return res


    def __repr__(self):
        if self.type_t == "query":
            res = ", ".join([repr(x) for x in self.premise])
        elif self.type_t == "fact":
            res = ", ".join([repr(x) for x in self.inference])
        else:
            res = ", ".join([repr(x) for x in self.inference]) + ":-" + ", ".join([repr(x) for x in self.premise])
        return res


    def __hash__(self):
        return hash(repr(self))


    @property
    def type_t(self):        
        if len(self.premise) == 0:  return "fact"
        elif len(self.inference) == 0:  return "query"
        else: return "rule"


    @property
    def var_list(self):
        res = []
        for p in self.premise:
            res += p.var_list
        res = list(dict.fromkeys(res))  # Remove duplicate variable
        return res


    @staticmethod
    def factory_complex_rule(string):
        #-----------Internal Func-----------
        # Apply distribution rule and generate every conjunction
        def distribute(premises):
            return distribute_disjunction(premises)

        def distribute_disjunction(premises):
            # This function only receive string, not a list
            # Split disjunction
            splitted = algebra_split(premises, ";")
            for p in splitted:
                for p1 in distribute_conjunction([p]):
                    yield p1 

        def distribute_conjunction(premises):
            if len(premises) == 1:
                # Split conjunction
                splitted = algebra_split(premises[0], ",")
                
                # If failed, then there might be a parenthesis put around the whole premise
                # or this is a predicate
                if len(splitted) == 1:
                    if splitted[0][0] == "(":
                        for p in distribute_disjunction(splitted[0][1:-1]):
                            yield p
                    else:
                        yield splitted[0]
                else:
                    for p in distribute_conjunction(splitted):
                        yield p
            else:
                for p in distribute_disjunction(premises[0]):
                    for p1 in distribute_conjunction(premises[1:]):
                        yield p+","+p1
        #-----------End intl func-----------

        # Remove every whitespace from string
        string = string.translate({ord(c): None for c in whitespace})

        # Break down a string into 2 parts: inference and premise
        inference, premises = tuple(string.split(":-",1))
    
        for p in distribute(premises):
            yield Sentence(inference+":-"+p)


    def infere(self, predicates):
        if type(predicates) != list:
            tmp = [predicates]
        else:
            tmp = predicates

        for p1 in tmp:
            found = False
            for p2 in self.inference:
                if p1.op == p2.op:
                    found = True
                    break
            if not found: return False
        
        return True


    def sub(self, theta):
        res = Sentence()
        res.inference = [p.sub(theta) for p in self.inference]
        res.premise = [p.sub(theta) for p in self.premise]
        return res


    def standardize(self, args):
        if type(args) != set:
            raise TypeError("standardize only accept set of strings.")
        
        trans = {}

        for v in self.var_list:
            if v in args:
                new_v = v
                while new_v in args:
                    new_v = new_v + "%"
                trans[v] = Term(new_v)

        return self.sub(trans)