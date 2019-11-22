import ast

def fileReadCode(filepath):
    content = []
    try:
        filecontent = open(filepath, mode="r", encoding="utf-8")
        for line in filecontent.readlines():
            if "//" in line:
                line = line.split("//")
                line = line[0]
            iterator = line.strip().replace("\n", "").split(" ")
            for el in iterator:
                if el != "":
                    content.append(el)
        content = '@'.join(content)
        return content
    except IOError as identifier:
        print(str(identifier))
    finally:
        filecontent.close()

def fileRead(filepath):
    try:
        filecontent = open(filepath, mode="r", encoding="utf-8")
        return filecontent.readlines()
    except IOError as identifier:
        print(str(identifier))
    finally:
        filecontent.close()
        
def getFileGrammar(filepath):
    try:
        content = []
        filecontent = open(filepath, mode="r", encoding="utf-8")
        for line in filecontent.readlines():
            content.append(line.rstrip('\n').split(','))
        return content
    except IOError as identifier:
        print(str(identifier))
    finally:
        filecontent.close()