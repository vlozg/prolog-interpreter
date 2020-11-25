from sentence import Sentence
from back_chaining import fol_ask

class KB:
    '''
    Knowledge base type. Contain all setences of rules and facts.
    '''
    def __init__(self):
        self.rules = []
        self.facts = []

    def add(self, string):
        # If a string contain infere symbol, then it is a rule
        if ":-" in string:
            for rule in Sentence.factory_complex_rule(string):
                self.rules.append(rule)
        else:
            fact = Sentence(string)
            self.facts.append(fact)

    def query(self, s):
        # The string must not end with dot.
        if type(s) == str:
            q = Sentence(s, is_query=True)
        else:
            q = s
        return fol_ask(self, q)