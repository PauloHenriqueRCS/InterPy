import io
import re


def fileread(filepath):
    try:
        fstr = []
        filecontent = open(filepath, mode="r", encoding="utf-8")
        for line in filecontent:
            if line.find("//") == -1:
                fstr.append(re.sub("\s+", " ", line).strip().split(";"))
            else:
                continue
        return fstr
    except IOError as identifier:
        print(str(identifier))
    finally:
        filecontent.close()


if __name__ == "__main__":
    filestr = fileread("../outFiles/teste.xul")
    print(filestr)
