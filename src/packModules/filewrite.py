def filewrite(outcontent,filename):
    try:
        filecontent = open("outFiles/outcontent.txt", mode="a", encoding="utf-8")
        filecontent.write("\n\n\n=========={}==========\n".format(filename))
        filecontent.write("\n".join(str(el) for el in outcontent))
    except IOError as identifier:
        print(str(identifier))
    finally:
        filecontent.close()
        
def fileLexWrite(outcontent,filename):
    try:
        filenameoutput = "outFiles/lex/lex{}.txt".format(filename)
        filecontent = open(filenameoutput, mode="w", encoding="utf-8")
        filecontent.write("\n".join(str(el) for el in outcontent))
    except IOError as identifier:
        print(str(identifier))
    finally:
        filecontent.close()
        
def fileSynWrite(outcontent,filename):
    try:
        filenameoutput = "outFiles/syn/syn{}.txt".format(filename)
        filecontent = open(filenameoutput, mode="w", encoding="utf-8")
        filecontent.write("".join(str(el) for el in outcontent))
    except IOError as identifier:
        print(str(identifier))
    finally:
        filecontent.close()

