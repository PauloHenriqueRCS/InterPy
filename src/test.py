from packModules.fileread import fileread
from packModules.lexical import Lexical


if __name__ == "__main__":
    lexical = Lexical()
    tokens = fileread("outFiles/teste7.xul")
    tlist = lexical.validating(tokens)
    lexical.tokenlistprint(tlist)