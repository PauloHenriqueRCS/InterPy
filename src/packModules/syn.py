import re
import ast

class Rule:
    def __init__(self, sym, prod):
        self.sym = sym
        self.prod = prod
        
class Syn:    
    def __init__(self):
        self.tokens = []
        self.rules = []
        self.batt = []
        self.logic = re.compile('(=|>=|<=|>|<|\=+|!=|\+|\-|\*|\/|\%)')
        self.symbols = re.compile('\(|\)|\[|\]|\;')
        self.error = False
                
    def empty(self):
        return False if len(self.tokens) > 0 else True

    def next(self):
        self.tokens.pop(0)
    
    def current_token(self):
        return self.tokens[0]
    
    def current_batt(self):
        return self.batt[-1]
    
    def charge(self, list_tokens, list_rules):
        self.error = False
        self.tokens = []
        self.batt = []
        (key), = ast.literal_eval(list_tokens[-1].rstrip()).keys()
        if key != 'error':
            for token in list_tokens:
                (key), = ast.literal_eval(token.rstrip()).keys()
                self.tokens.append(key)
            for rule in list_rules:
                self.rules.append(Rule(rule[0],rule[1]))
            self.batt.append(self.rules[0].sym)
        else:
            self.error = True
            
    def match(self, sym1, sym2):
        if self.logic.search(sym2) is not None:
            return  self.logic.findall(sym2)
        elif self.symbols.search(sym2) is not None:
            return self.symbols.findall(sym2)
        match = re.compile(sym1)
        return match.search(sym2)
            
    def proc(self):
        if len(self.tokens) > 0:
                for x in range (0, len(self.tokens)):
                    self.aTerminalMatch()
        
    def aTerminalMatch(self):
        for rule in self.rules:
            if self.current_batt() == rule.sym:
                if self.current_token() in rule.prod:
                    self.batt.append(rule.prod)
                    self.terminalMatch()
    
    def terminalMatch(self):
        for rule in self.rules:
            if self.current_batt() == rule.prod:
                if self.current_token() in rule.prod:
                    temp = rule.prod[0:-1]
                    if temp == self.current_token():
                        self.batt.append(rule.prod[len(temp):])
                        self.next()
                        self.proc()
            
    def analysis(self, list_tokens, list_rules):
        self.charge(list_tokens, list_rules)  
        if self.error is not True:  
            self.proc()
            list_tokens.pop(-1)
            if len(self.tokens) > 1:
                erro = "token <{}> syntatic error.".format(self.current_token())
                list_tokens.append(dict({'error': erro}))
            return list_tokens
        else:
            return 'this file contains lex error!'
            