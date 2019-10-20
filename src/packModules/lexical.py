import re


class Lexical:
    def __init__(self):
        self.lexeme = ''
        self.tokens_list = []
        self.in_text = False
        self.symbols = re.compile('\(|\)|\{|\}|\[|\]|\;')
        self.key_words = re.compile(
            'int|float|double|string|True|False|bool|if|else|for|while|break|return')
        self.id = re.compile('[a-zA-Z0-9_]+')
        self.logic = re.compile('(=|>=|<=|>|<|==|!=|\+|\-|\*|\/|\%)')
        self.decimal = re.compile('[0-9]+[.][0-9]+|[0-9]+[.]|[.][0-9]+')
        self.digit = re.compile('[0-9]+')
        self.text = re.compile('([\w])+')
        self.aspas = re.compile('\"|\'')
        self.symbols_dict = {
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
            '-': '-',
            '*': '*',
            '/': '/',
            '%': '%',
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

    def isSymbol(self, lexeme):
        return True if self.symbols.search(lexeme) is not None else False

    def isKeyword(self, lexeme):
        return True if self.key_words.search(lexeme) is not None else False

    def isDigit(self, lexeme):
        return True if self.digit.search(lexeme) is not None else False

    def isDecimal(self, lexeme):
        return True if self.decimal.search(lexeme) is not None else False

    def isId(self, lexeme):
        return True if self.id.search(lexeme) is not None else False

    def isLogic(self, lexeme):
        return True if self.logic.search(lexeme) is not None else False

    def isDelimiter(self, lexeme):
        return True if lexeme is '@' else False

    def isText(self, lexeme):
        return True if self.aspas.search(lexeme) is not None else False

    def addToken(self, symdict='id'):
        self.tokens_list.append(dict({self.symbols_dict[symdict]: self.lexeme}))
        self.lexeme = ''

    def validating(self, content):
        self.lexeme = ''
        self.tokens_list = []
        for lex in range(0, len(content)):
            if self.isDelimiter(content[lex]) is False:
                self.lexeme += content[lex]
                if self.isSymbol(self.lexeme) is False:
                    if self.isText(content[lex]):
                        self.in_text = True if self.in_text is False else False
                        if self.in_text is False:
                            self.lexeme = self.lexeme.replace('"', "", 2)
                            self.addToken()
                            self.in_text = False
                            continue
                    elif self.isText(self.lexeme) is False and self.in_text is False:
                        if self.isKeyword(self.lexeme) and (self.isDelimiter(content[lex + 1]) or self.isSymbol(content[lex + 1])):
                            self.addToken(self.lexeme)
                            continue
                        elif self.isKeyword(self.lexeme):
                            self.addToken(self.lexeme)
                            continue
                        elif ((self.isDigit(self.lexeme)) or (self.isDecimal(self.lexeme))) and ((self.isSymbol(content[lex + 1])) or (self.isLogic(content[lex + 1])) or (self.isId(content[lex + 1]) is False)):
                            if content[lex + 1] != '.':
                                self.addToken()
                                continue
                        elif self.isLogic(self.lexeme):
                            if self.isLogic(content[lex + 1]) is False:
                                self.addToken(self.lexeme)
                            else:
                                continue
                        elif self.isId(self.lexeme):
                            if ((self.isSymbol(content[lex + 1])) or self.isDelimiter(content[lex + 1])) or ((self.isLogic(content[lex + 2])) or (self.isLogic(content[lex + 1]))):
                                self.addToken()
                                continue
                            elif self.isId(content[lex + 1]) is False:
                                self.addToken()
                                continue
                        else:
                            erro = "ERROR: token <{}> not a valid symbol.".format(
                                self.lexeme)
                            self.tokens_list.append(erro)
                            #self.tokens_list.append(dict({self.lexeme: 'not a valid symbol.'}))
                            return self.tokens_list
                            #raise ValueError(erro)
                else:
                    self.addToken(self.lexeme)
            else:
                if self.in_text is False:
                    self.lexeme = ''
                else:
                    self.lexeme += " "
        return self.tokens_list

    def tokenlistprint(self, tokenList):
        print(tokenList)
