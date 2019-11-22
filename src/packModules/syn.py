import ast
from packModules.battery import Battery

class Rule:
    def __init__(self, sym, prod):
        self.sym = sym
        self.prod = prod
        
class Syn:    
    def __init__(self):
        self.tokens = []
        self.rules = []
        self.batt = Battery()
                
    def charge(self, list_tokens, list_rules):
        for token in list_tokens:
            (key), = ast.literal_eval(token.rstrip()).keys()
            self.tokens.append(key)
        for rule in list_rules:
            self.rules.append(Rule(rule[0],rule[1]))
        self.batt.add(self.rules[0])

    def empty(self):
        return False if len(self.tokens) > 0 else True

    def next(self):
        self.tokens.pop(0)
    
    def current_token(self):
        return self.tokens[0]

    def leave(self):
        if self.batt.top() == self.current_token():
            self.batt.remove()
            
    def analysis(self, list_tokens, list_rules):
        self.charge(list_tokens, list_rules)           
            