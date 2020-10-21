def createWordList(filePath):
    list = []
    file = open(filePath, "r")
    line = file.readline()
    while line is not "":
        list.append(line.rstrip("\n"))
        line = file.readline()
    return list

print(createWordList("wordlist.txt"))