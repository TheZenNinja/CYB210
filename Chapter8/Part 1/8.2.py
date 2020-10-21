def createWordSet(filePath):
    mySet = set()
    file = open(filePath, "r")
    line = file.readline()
    while line is not "":
        mySet.add(line.rstrip("\n"))
        line = file.readline()
    return mySet

print(createWordSet("wordlist.txt"))