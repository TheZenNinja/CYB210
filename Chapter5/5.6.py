numOfLines = 0
numOfWords = 0
numOfChars = 0
import re
def CountFile(fileName):
    file = open(fileName, "r")

    fileTxt = file.read()
    numOfLines = len(fileTxt.split("\n"))
    
    words = re.split("\n| ",fileTxt)
    numOfWords = len(words)
    
    numOfChars = len(fileTxt)
    
    print("Lines: %i" % numOfLines, "\nWords: %i" % numOfWords,"\nCharacters: %i" % numOfChars)

CountFile("5.5 Input.txt")