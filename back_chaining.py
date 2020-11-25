from sentence import Sentence
from unify import unify
from utility import extract_keys

def fol_ask(kb, query):
    '''
    Answer the query base on the knowledge base.

    Param:
    -   kb (KB): knowledge base.
    -   query (Sentence).

    Return
    +   (dict generator): all substitutions satisfy the query.
        Special returned value:
        -   Returned None: there is not an answer satisfy the query.
        -   Returned empty dict: the current query is a fact (any substitute can satisfy).
    '''
    if len(query.premise) > 1:
        return fol_and(kb, query.premise, {})
    else:
        return fol_or(kb, query.premise[0], {})


def fol_or(kb, goal, theta):
    '''
    Find a substitution satisfy the single query base on knowledge base.

    Param:
    -   kb (KB): knowledge base.
    -   goal (Predicate): single query, only accept one predicate.
    -   theta (dict): substitution built up so far.

    Return
    -   (dict generator)
    '''
    # Returned substitution only contain keys of this goal variables and of theta built up to the current.
    # So var_keep is a list of variable name to keep.
    var_keep = goal.var_list + list(theta.keys())


    # Special case: unify relation
    if goal.op == "=":
        theta_t = unify(goal.args[0], goal.args[1], dict(theta))
        # If substitution found and this is unify => that unify satisfy this query
        #   or cannot unify and this is not equal relation => the current unify satisfy this query
        if theta_t is not None and goal.truth:
            yield extract_keys(theta_t,var_keep)
        elif theta_t is None and not goal.truth:
            yield theta
        return
    
    
    # Normal fol_or
    for rule in fetch_rule(kb, goal):
        # Standardize and divide in to 2 part: left hand side and right hand side.
        rule_s = rule.standardize(set(var_keep))
        left= rule_s.premise
        # Only take the needed inference on the right hand side
        for p in rule_s.inference:
            if p.op == goal.op:
                right = p
                break

        # Find theta1 that:
        # - Satisfy all predicate on the left hand side
        # - Make right hand side same as goal
        for theta1 in fol_and(kb, left, unify(right, goal, dict(theta))):
            yield extract_keys(theta1, var_keep)
        
        pass # implement not in the future


def fol_and(kb, goal, theta):
    '''
    Find a substitution satisfy multiple queries base on knowledge base.

    Param:
    -   kb (KB): knowledge base.
    -   goal (list of Predicate): multiple queries.
    -   theta (dict): substitution built up so far.

    Return
    -   (dict generator)
    '''
    if theta is None: return
    elif len(goal) == 0: yield theta
    else:
        first, rest = goal[0], goal[1:]
        for theta1 in fol_or(kb, first.sub(theta), theta):
            for theta2 in fol_and(kb, rest, theta1):
                yield theta2


def fetch_rule(kb, goal):
    '''
    Fetch all rules that infere goal.

    Param:
    -   kb (KB): knowledge base
    -   goal (Predicate): rule found must infere this.

    Return:
    -   (Sentence - generator) all rules infere goal.
    '''
    # Finding unit clause first
    for fact in kb.facts:
        if fact.infere(goal):
            yield fact

    for rule in kb.rules:
        if rule.infere(goal):
            yield rule