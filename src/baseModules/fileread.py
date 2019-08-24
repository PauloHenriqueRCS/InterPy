import io


def fileread(filepath):
    try:
        filecontent = io.open(filepath, mode="r", encoding="utf-8").read()
        return filecontent
    except IOError as identifier:
        print(str(identifier))
