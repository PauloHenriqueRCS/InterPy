from packModules.fileread import fileReadCode
from packModules.fileread import fileRead, getFileGrammar
from packModules.filewrite import filewrite
from packModules.lex import Lex
from packModules.syn import Syn

def writeresults(results, filename):
    filewrite(results, filename)

def lexAnalysis(lex):
    for index in range(1, 11):
        filename = "outFiles/teste{}.xul".format(index)
        filecontent = fileReadCode(filename)
        tokenlist = lex.analysis(filecontent)
        writeresults(tokenlist, filename)

def synAnalysis(syn):
        filename = "outFiles/synTest.txt"
        filecontentT = fileRead(filename)
        filename = "dfa/Grammar.txt"
        filecontentG = getFileGrammar(filename)
        syn.analysis(filecontentT, filecontentG)


if __name__ == "__main__":
    #lex = Lex()
    #lexAnalysis(lex)
    syn = Syn()
    synAnalysis(syn)
        