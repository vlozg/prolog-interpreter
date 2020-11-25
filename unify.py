from term import *

def unify(x, y, theta = {}):
	'''
	Take 2 compound expressions and return a substitution if exist.

	Param: 
		x, y: variable, constant, list or compound expression.
		theta: the substitution built up so far.

	Return:
		Substitution found or None when not exist.
    '''
	
	# Failed to find a substitution
	if theta is None:
		return None

	# X and Y is identical -> this theta substitution is correct
	elif x == y:	
		return theta

	# Do unfication on variable if either x or y is variable
	elif is_variable(x): 
		return unify_var(x, y, theta)
	elif is_variable(y):
		return unify_var(y, x, theta)

	# If both X and Y is in the form F(A, B) then unify the list of variables (unify (A, B))
	elif is_compound(x) and is_compound(y): 
		return unify(x.args, y.args, unify(x.op, y.op, theta))

	# If both x and y is list
	# -> Unify the first one of both, then unify the rest with the substitution found
	elif type(x) is list and type(y) is list:   
		return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    
	# Usually this case is reached when compare the op of 2 compound expressions.
	else:
		return None 



def unify_var(var, x, theta):
	'''
	Unify 1 variable with 1 expression, return a substitution if exist.
	'''
	if var.op in theta:
		# There is a sub for var exist
		return unify(theta[var.op], x, theta)
	
	elif is_variable(x) and x.op in theta:
		# x is variable and there is a sub for x exist
		return unify(var, theta[x.op], theta)
	
	elif check_recursive(var, x):
		return None
	
	else:
		# Add new record to theta
		theta[var.op] = x
		return theta



def check_recursive(var, x):
	if type(x) in [Predicate, Term]:
		return var.op in x.var_list
	return False



def is_variable(x):
	if type(x) == Term:
		if x.type_t == "variable":
			return True
	return False



def is_compound(x):
	if type(x) in [Term, Predicate]:
		if x.args is not None:
			return True
	return False