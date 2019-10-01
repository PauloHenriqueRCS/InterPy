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
            "bit": "bit",
            "decimal": "decimal",
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

    def match(self, tokens):
        key_list = self.symbols.keys()
        for tc in tokens:
            if tc in key_list:
                print("token <" + tc + "> esta presente em symbols.\n")
            else:
                print("token <" + tc + "> nao esta presente em symbols.\n")
