def filewrite(outcontent,filename):
    try:
        filecontent = open("outFiles/outcontent.txt", mode="a", encoding="utf-8")
        filecontent.write("\n\n\n=========={}==========\n".format(filename))
        filecontent.write("\n".join(str(el) for el in outcontent))
    except IOError as identifier:
        print(str(identifier))
    finally:
        filecontent.close()
