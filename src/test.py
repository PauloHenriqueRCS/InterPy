from packModules.fileread import fileReadCode
from packModules.fileread import fileRead, getFileGrammar
from packModules.filewrite import fileLexWrite, fileSynWrite
from packModules.lex import Lex
from packModules.syn import Syn


def lexAnalysis(lex):
    for index in range(1, 11):
        filename = "outFiles/teste{}.xul".format(index)
        filecontent = fileReadCode(filename)
        tokenlist = lex.analysis(filecontent)
        fileLexWrite(tokenlist, "teste{}".format(index))

def synAnalysis(syn):
    for index in range(1, 11):
        filename = "outFiles/lex/lexteste{}.txt".format(index)
        filecontentT = fileRead(filename)
        filenameG = "dfa/Grammar.txt"
        filecontentG = getFileGrammar(filenameG)
        tokenlist = syn.analysis(filecontentT, filecontentG)
        fileSynWrite(tokenlist, "teste{}".format(index))


if __name__ == "__main__":
    #lex = Lex()
    #lexAnalysis(lex)
    syn = Syn()
    synAnalysis(syn)
        