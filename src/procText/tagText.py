
import io
import re
from fileRW import fileR

def tagText(filePath):
    str = re.sub("\s+", " ", fileR(filePath)).split(" ")
    return str
