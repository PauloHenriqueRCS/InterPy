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
        self.key_list = self.symbols.keys()
        self.type_list = ['int', 'float', 'double', 'str', 'kw', 'bool']
        self.logical_list = ['=', '<', '>', '<=', '>=', '!=', '==']
       
    def tonumber(self, number):
        try:
            float(self.number)
            return True
        except ValueError:
            pass
        return False

    def match(self, tokens):
        prev = next(iter(self.key_list))
        for tc in tokens:
            if tc in self.key_list:
                prev = tc
                continue
            else:
                if prev in self.type_list and prev != '=' and tc.isdigit():
                    raise ValueError("token <{}> not a symbol.\n".format(tc))
            prev = tc

    def matchprint(self, tokens):
        prev = next(iter(self.key_list))
        for tc in tokens:
            if tc in self.key_list:
                print("token <{}> is a symbol.\n".format(tc))
            else: #Necessario corrigir como faremos para validar o symbol id direito
                if prev in self.key_list:
                    if tc.isdigit() is False:
                        print("token <{}> is a symbol.\n".format(tc))
                    elif prev in ['[', ']', '(', ')'] and tc.isdigit():
                        print("token <{}> is a symbol.\n".format(tc))
                    elif prev in self.logical_list and tc.isdigit():
                        print("token <{}> is a symbol.\n".format(tc))
                    elif prev in self.type_list and tc.isdigit():
                        print("token <{}> not a symbol.\n".format(tc))
                else:
                    print("token <{}> not a symbol.\n".format(tc))
            prev = tc
