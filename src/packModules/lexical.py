import re


class Lexical:
    def __init__(self):
        self.lexeme = ''
        self.tokenslist = []
        self.inText = False
        self.symbols = re.compile('\(|\)|\{|\}|\[|\]|\;')
        self.keywords = re.compile(
            'int|float|double|string|True|False|bool|if|else|for|while|break|return')
        self.id = re.compile('[a-zA-Z0-9_]+')
        self.logic = re.compile('(=|>=|<=|>|<|==|!=|\+|\-|\*|\/)')
        self.decimal = re.compile('[0-9]+[.][0-9]+|[0-9]+[.]|[.][0-9]+')
        self.digit = re.compile('[0-9]+')
        self.text = re.compile('([\w])+')
        self.aspas = re.compile('\"|\'')
        self.symbolsdict = {
            '{': '{',
            '}': '}',
            '(': '(',
            ')': ')',
            '[': '[',
            ']': ']',
            'int': 'int',
            'float': 'float',
            'bool': 'bool',
            'string': 'string',
            'double': 'double',
            'True': 'True',
            'False': 'False',
            'if': 'if',
            'else': 'else',
            'while': 'while',
            'break': 'break',
            'for': 'for',
            '=': '=',
            '+': '+',
            '<': '<',
            '>': '>',
            '>=': '>=',
            '<=': '<=',
            '!=': '!=',
            '==': '==',
            '||': '||',
            'id': 'id',
            'num': 'num',
            ';': ';',
        }

    def issymbol(self, lexeme):
        return True if self.symbols.search(lexeme) is not None else False

    def iskeyword(self, lexeme):
        return True if self.keywords.search(lexeme) is not None else False

    def isdigit(self, lexeme):
        return True if self.digit.search(lexeme) is not None else False

    def isdecimal(self, lexeme):
        return True if self.decimal.search(lexeme) is not None else False

    def isid(self, lexeme):
        return True if self.id.search(lexeme) is not None else False

    def islogic(self, lexeme):
        return True if self.logic.search(lexeme) is not None else False

    def isdelimiter(self, lexeme):
        return True if lexeme is '@' else False

    def istext(self, lexeme):
        return True if self.aspas.search(lexeme) is not None else False
    
    def addtoken(self, symdict = 'id'):
        self.tokenslist.append(dict({self.symbolsdict[symdict]: self.lexeme}))
        self.lexeme = ''

    def validating(self, content):
        for lex in range(0, len(content)):
            if self.isdelimiter(content[lex]) is False:
                self.lexeme += content[lex]
                if self.issymbol(self.lexeme) is False:
                    if self.istext(content[lex]):
                        self.inText = True if self.inText is False else False
                        if self.inText is False:
                            self.lexeme = self.lexeme.replace('"', "", 2)
                            self.addtoken()
                            self.inText = False
                            continue
                    elif self.istext(self.lexeme) is False and self.inText is False:
                        if self.iskeyword(self.lexeme) and (self.isdelimiter(content[lex + 1]) or self.issymbol(content[lex + 1])):
                            self.addtoken(self.lexeme)
                            continue
                        elif ((self.isdigit(self.lexeme)) or (self.isdecimal(self.lexeme) )) and ((self.issymbol(content[lex + 1])) or (self.islogic(content[lex + 1])) or (self.isid(content[lex + 1]) is False)):
                            if content[lex + 1] != '.':
                                self.addtoken()
                                continue
                        elif self.isid(self.lexeme):
                            if ((self.issymbol(content[lex + 1])) or self.isdelimiter(content[lex + 1]) ) or ((self.islogic(content[lex + 2])) or (self.islogic(content[lex + 1]))):
                                self.addtoken()
                                continue
                        elif self.islogic(self.lexeme):
                            if self.islogic(content[lex + 1]) is False:
                                self.addtoken(self.lexeme)
                            else:
                                continue
                        else:
                            raise ValueError(
                                "token <{}> not a symbol.\n".format(self.lexeme))
                else:
                    self.addtoken(self.lexeme)
            else: 
                if self.inText is False:
                    self.lexeme = '' 
                else:
                    self.lexeme += " "
        return self.tokenslist

    def tokenlistprint(self, tokenList):
        print(tokenList)
