
import io
import re
from fileRW.fileR import fileR

def tagTextAlt(filePath):
    strElements = fileR(filePath).splitlines()
    print(strElements)

    for element in strElements:
        element = " " if element.find("//") == 1 else element


    print(strElements)
