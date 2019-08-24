import io

def fileR(fielPath):
    try:
        file = io.open(fielPath, mode="r", encoding="utf-8")
        return file.read()
        file.close()
    except IOError as identifier:
        print(str(identifier))
   
