import io
import re


def fileopen(fileopen):
    try:
        file = io.open(fileopen, mode="r", encoding="utf-8")
        s = re.sub("\s+", " ", file.read()).split(" ")
        return s
    except IOError as identifier:
        print(str(identifier))
    finally:
        file.close()


if __name__ == "__main__":
    str = fileopen("words.txt")
    print(str)
