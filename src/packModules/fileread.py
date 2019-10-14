def fileread(filepath):
    content = []
    try:
        filecontent = open(filepath, mode="r", encoding="utf-8")
        for line in filecontent.readlines():
            if "//" in line:
                line = line.split("//")
                line = line[0]
            iterator = line.strip().replace("\n", "").split(" ")
            for el in iterator:
                if el != "":
                    content.append(el)
        content = '@'.join(content)
        return content
    except IOError as identifier:
        print(str(identifier))
    finally:
        filecontent.close()
