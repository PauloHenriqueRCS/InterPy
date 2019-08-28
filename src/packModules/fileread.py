import io

def fileread(filepath):
    try:
        fstr = []
        filecontent = open(filepath, mode="r", encoding="utf-8")
        for line in filecontent:
            if line.find("//") == -1:
                fstr.append(line)
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
