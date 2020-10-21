import time
def createWordDict(dname):
    myDict = {}
    myFile = open(dname, 'r')
    for line in myFile:
        myDict[line [: -1]] = True
    return myDict

def createWordList(filePath):
    list = []
    file = open(filePath, "r")
    line = file.readline()
    while line is not "":
        list.append(line.rstrip("\n"))
        line = file.readline()
    return list

def createWordSet(filePath):
    mySet = set()
    file = open(filePath, "r")
    line = file.readline()
    while line is not "":
        mySet.add(line.rstrip("\n"))
        line = file.readline()
    return mySet

startTime = time.time()
createWordDict("wordlist.txt")
endTime = time.time()
print("createWordDict took", endTime - startTime, "seconds")

startTime = time.time()
createWordList("wordlist.txt")
endTime = time.time()
print("createWordList took", endTime - startTime, "seconds")

startTime = time.time()
createWordSet("wordlist.txt")
endTime = time.time()
print("createWordSet took", endTime - startTime, "seconds")