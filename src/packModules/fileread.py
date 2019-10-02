import io


def treatmentcontent(filecontent):
    contentlist = []
    for line in filecontent:
        if line.find("//") == -1:
            iterator = line.strip().replace("\n", "").split(" ")
            for el in iterator:
                if el != "":
                    if ';' in el:
                        contentlist.append(el[:-1])
                        contentlist.append(el[len(el)-1])
                    else:
                        contentlist.append(el)
    return contentlist


def fileread(filepath):
    try:
        filecontent = open(filepath, mode="r", encoding="utf-8")
        return treatmentcontent(filecontent)
    except IOError as identifier:
        print(str(identifier))
    finally:
        filecontent.close()
