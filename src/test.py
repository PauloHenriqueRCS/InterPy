from packModules.fileread import fileread
from packModules.matchsymbols import Matchsymbols


if __name__ == "__main__":
    MS = Matchsymbols()
    tokens = fileread("outFiles/teste.xul")
    print(tokens)
    MS.matchprint(tokens)   
