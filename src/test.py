from packModules.fileread import fileread



tb = {
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

def matchSymbols(tokens):
    key_list = tb.keys()
    for tc in tokens:
        if tc in key_list:
            print(tc)


if __name__ == "__main__":
    tokens = fileread("outFiles/teste.xul")
    print(tokens)
    #matchSymbols(tokens)
   
