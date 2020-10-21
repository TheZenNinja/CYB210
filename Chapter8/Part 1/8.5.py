def createWordDict(dname):
    myDict = {}
    myFile = open(dname, 'r')
    for line in myFile:
        myDict[line [: -1]] = True
    return myDict

def railDecrypt(cipherTxt, railNum):
    railLen = len(cipherTxt)//railNum
    plainTxt = ""
    for col in range(railLen):
        for rail in range(railNum):
            nextletter = col + rail * railLen;
            plainTxt += cipherTxt[nextletter]
    return plainTxt.split()

def railBreak(cipherText):
    wordDict = createWordDict('wordlist.txt')
    cipherLen = len(cipherText)
    maxGoodSoFar = 0
    bestGuess = "No words found in dictionary"
    for i in range (1, cipherLen +1):
        words = railDecrypt(cipherText,i)
        goodCount = 0
        for w in words :
            if w in wordDict:
                goodCount = goodCount + 1
        if goodCount > maxGoodSoFar :
            maxGoodSoFar = goodCount
            bestGuess = " ".join(words)
    return bestGuess

file = open("ch8-ciphertext.txt", "r")

#print(railBreak("ts e   od eie  no srghou s nsgb dta ein tphv eyyaowhtg ahaeaht oymyeshynec desou"))

for line in file:
    print(railBreak(line))