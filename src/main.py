import io
import re
import sys
from procText.tagText import tagText
from procText.tagTextAlt import tagTextAlt

def proc(fileopen):
    return tagTextAlt(fileopen)

if __name__ == "__main__":
    str = proc("../outFiles/teste.xul")

    print(str)
