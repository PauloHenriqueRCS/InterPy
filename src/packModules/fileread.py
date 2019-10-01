import io
import re

def splitintags(line):
    return re.sub("\s+", " ", line.split(" "))

def fileread(filepath):
    try:
        fstr = []
        filecontent = open(filepath, mode="r", encoding="utf-8")
        for line in filecontent:
            if line.find("//") == -1:
                liststr = line.split(" ")
                for el in liststr:
                    if el != "":
                        if ';' in el:
                            fstr.append(el[:-1])
                            fstr.append(el[-1:])
                        else:
                            fstr.append(el)
                    else:
                        continue
            else:
                continue
        return fstr
    except IOError as identifier:
        print(str(identifier))
    finally:
        filecontent.close()

def filereadalt(filepath):
    try:
        filecontent = io.open(filepath, mode="r", encoding="utf-8").read()
        return filecontent
    except IOError as identifier:
        print(str(identifier))
