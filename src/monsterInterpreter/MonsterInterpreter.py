import io

class MonsterInterpreter:
    def __init__(self, filePath=""):
        self.filePath = filePath
        self.fileContent

    def fileRead(self, fielePath):
        self.filePath = filePath
        
    try:
        fileObj = io.open(self.filePath, mode="r", encoding="utf-8")
        self.fileContent = fileObj.read()
    except IOError as identifier:
        print(str(identifier))
