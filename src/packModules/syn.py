import ast

class Syn:
    def __init__(self):
        self.tokens = []

    def charge(self, list_tokens):
        for token in list_tokens:
            (key), = ast.literal_eval(token.rstrip()).keys()
            self.tokens.append(key)

    def empty(self):
        return False if len(self.tokens) > 0 else True

    def next(self):
        self.tokens.pop(0)
    
    def current_token(self):
        return self.tokens[0]

    def analysis(self, list_tokens):
        list_tokens
        self.charge(list_tokens)
        print(self.current_token())
        self.next()
        print(self.current_token())

    def productionA(self):
        self.tokens