from packModules.fileread import fileread
from packModules.matchsymbols import Matchsymbols


if __name__ == "__main__":
    MS = Matchsymbols()
    tokens = fileread("outFiles/teste.xul")
    #MS.match(tokens)
    #matchSymbols(tokens)
   
