import re

def splitintags(filecontent):
        return re.sub("\s+", " ", filecontent.split(" "))
