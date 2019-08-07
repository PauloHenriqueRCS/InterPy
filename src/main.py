import io
import re


def fileopen(fileopen):
    try:
        file = io.open(fileopen, mode="r", encoding="utf-8")
        return file.read()
    except IOError as identifier:
        print(str(identifier))
    finally:
        file.close()


if __name__ == "__main__":
    str = fileopen("src/words.txt")
    s = re.sub("\s+", " ", str).split(" ")
    print(s)
