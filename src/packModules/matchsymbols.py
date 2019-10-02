class Matchsymbols:
    def __init__(self):
        self.symbols = {
            "{": "{",
            "}": "}",
            "(": "(",
            ")": ")",
            "[": "[",
            "]": "]",
            "id": str,
            ";": ";",
            "kw": "kw",
            "int": "int",
            "float": "float",
            "bool": "bool",
            "str": "str",
            "double": "double",
            "true": "true",
            "false": "false",
            "if": "if",
            "while": "while",
            "break": "break",
            "=": "=",
            "+": "+",
            "<": "<",
            ">": ">",
            ">=": ">=",
            "<=": "<=",
            "!=": "!=",
            "==": "=="
        }

    def tonumber(self, number):
        try:
            float(self.number)
            return True
        except ValueError:
            pass
        return False

    def match(self, tokens):
        key_list = self.symbols.keys()
        prev = next(iter(key_list))
        for tc in tokens:
            if tc in key_list:
                prev = tc
                continue
            else:
                if (prev == 'int' or 'float' or 'double' or 'str' or 'kw' or 'bool') and (prev != '=') and (tc.isdigit()):
                    raise ValueError("token <{tk}> nao esta presente em symbols.\n".format(tk=repr(tc)))
            prev = tc

    def matchprint(self, tokens):
        key_list = self.symbols.keys()
        prev = next(iter(key_list))
        for tc in tokens:
            if tc in key_list:
                print("token <" + tc + "> esta presente em symbols.\n")
            else:
                if prev == 'int' or 'float' or 'double' or 'str' and tc.isdigit() is False:
                    print("token <{tk}> esta presente em symbols.\n".format(tk=repr(tc)))
                elif (prev == 'int' or 'float' or 'double' or 'str' or 'kw' or 'bool') and (prev != '=') and (tc.isdigit()):
                    print("token <{tk}> nao esta presente em symbols.\n".format(tk=repr(tc)))
                else:
                    print("token <{tk}> nao esta presente em symbols.\n".format(tk=repr(tc)))
            prev = tc
