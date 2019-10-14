import re


class Lexical:
    def __init__(self):
        self.symbols = re.compile('\(|\)|\{|\}|\[|\]|\;')
        self.keywords = re.compile(
            'int|float|double|True|False|bool|if|else|for|while|break|return')
        self.id = re.compile('[a-zA-Z0-9_]+')
        self.logic = re.compile('(=|>=|<=|>|<|==|!=|\+|\-|\*|\/)')
        self.decimal = re.compile('[0-9]+[.][0-9]+|[0-9]+[.]|[.][0-9]+')
        self.digit = re.compile('[0-9]+')
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
            'str': 'str',
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

    def validating(self, content):
        lexeme = ''
        tokensList = []

        for lex in range(0, len(content)):
            if content[lex] is not '@':
                is_symbol = self.symbols.search(content[lex])
                if not is_symbol:
                    lexeme += content[lex]
                    if self.keywords.search(lexeme) is not None and (content[lex + 1] is '@' or self.symbols.search(content[lex + 1])):
                        word = self.keywords.search(lexeme)
                        tokensList.append(
                            dict({self.symbolsdict[word.group()]: word.group()}))
                        lexeme = ''
                        continue
                    elif (self.digit.search(lexeme) is not None or self.decimal.search(lexeme) is not None) and ((self.symbols.search(content[lex + 1]) is not None) or (self.logic.search(content[lex + 1]) is not None)):
                        tokensList.append(
                            dict({self.symbolsdict['id']: lexeme}))
                        lexeme = ''
                        continue
                    elif self.id.search(lexeme) is not None:
                        if (content[lex + 1] is self.symbolsdict[';']) or (content[lex + 1] is '@' and self.logic.search(content[lex + 2]) is not None) or (self.logic.search(content[lex + 1]) is not None) or (self.symbols.search(content[lex + 1]) is not None) or content[lex + 1] is '@':
                            word = self.id.search(lexeme)
                            tokensList.append(
                                dict({self.symbolsdict['id']: word.group()}))
                            lexeme = ''
                            continue
                    elif self.logic.search(lexeme) is not None and self.logic.search(content[lex + 1]) is None:
                        word = self.logic.search(lexeme)
                        tokensList.append(
                            dict({self.symbolsdict[word.group()]: word.group()}))
                        lexeme = ''
                        continue
                    else:
                        raise ValueError(
                            "token <{}> not a symbol.\n".format(lexeme))
                else:
                    tokensList.append(
                        (dict({self.symbolsdict[is_symbol.group()]: is_symbol.group()})))
        return tokensList

    def tokenlistprint(self, tokenList):
        print(tokenList)
