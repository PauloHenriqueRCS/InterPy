import io
import re

class MonsterInterpreter:
    filepath: str
    filecontent: str
    fileobj: type(io)

    def __init__(self, filepath=""):
        self.filepath = filepath

    def fileread(self, filepath):
        self.filepath = filepath
        try:
            fileobj = io.open(self.filepath, mode="r", encoding="utf-8")
            self.filecontent = fileobj.read()
        except IOError as identifier:
            print(str(identifier))