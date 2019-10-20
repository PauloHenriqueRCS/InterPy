from packModules.fileread import fileread
from packModules.filewrite import filewrite
from packModules.lexical import Lexical

def writeresults(results, filename):
    filewrite(results, filename)

def procexemples(lexical):
    for index in range(1, 11):
        filename = "outFiles/teste{}.xul".format(index)
        filecontent = fileread(filename)
        tokenlist = lexical.validating(filecontent)
        writeresults(tokenlist, filename)

if __name__ == "__main__":
    lexical = Lexical()
    procexemples(lexical)
    #tokens = fileread("outFiles/teste9.xul")
    #tlist = lexical.validating(tokens)
    #writeresults(tlist, "outFiles/teste9.xul")
    #lexical.tokenlistprint(tlist)
        