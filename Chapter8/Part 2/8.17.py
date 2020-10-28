import re
def printMatch(match):
    if (match != None):
        print(match.string)
    else:
        print("Doesnt Match")


#17
match = re.search("s$", "words")
printMatch(match)
match = re.search("s$", "sell")
printMatch(match)
print()
#18
match = re.search("ing$", "ending")
printMatch(match)
match = re.search("ing$", "endings")
printMatch(match)
print()
#19
match = re.search(".*ss.*", "missing")
printMatch(match)
print()
#20
match = re.search("^st", "start")
printMatch(match)
match = re.search("^st", "past")
printMatch(match)
print()
#22
match = re.search("^.[aeiou]{2}.$", "loot")
printMatch(match)
match = re.search("^.[aeiou]{2}.$", "lute")
printMatch(match)
match = re.search("^.[aeiou]{2}.$", "lot")
printMatch(match)
match = re.search("^.[aeiou]{2}.$", "loose")
printMatch(match)