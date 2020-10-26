def letterCountDict(text):
    text = text.lower()
    nonLetters = removeMatches(text, "abcdefghijklmnopqrstuvwxyz")
    letters = removeMatches(text, nonLetters)
    myDict = {}
    for l in letters:
        if l not in myDict.keys():
            myDict[l] = 1
        else:
            myDict[l] += 1

    return myDict

def removeMatches(text, toRemove):
    newTxt = ""
    for l in text:
        if l not in toRemove:
            newTxt += l;
    return newTxt

print(letterCountDict("Hello"))