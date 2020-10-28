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
def neighborCount(text):
    nbDict = {}
    text = text.lower ()
    for i in range(len(text) -1):
        nbList = nbDict.setdefault(text [i], [])
        maybeAdd(text [i+1], nbList)
        nbList = nbDict.setdefault(text [i +1], [])
        maybeAdd(text [i], nbList)
    for key in nbDict :
        nbDict[key] = len(nbDict[key])
    return nbDict
def maybeAdd(ch, toList):
    if ch in 'abcdefghijklmnopqrstuvwxyz' and ch not in toList:
        toList.append (ch)



print(letterCountDict("Hello"))