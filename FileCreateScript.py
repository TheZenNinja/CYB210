chapterNum = int(input("Chapter: "))

inputFinished = False
sections = []

print("Type \"x\" to exit")
while not inputFinished:
    section = input("Section: ")
    if section == "x":
        inputFinished = True
        break;
    sections.append(section)


if sections != []:
    for name in sections:
        path = "Chapter" + str(chapterNum) + "/" + str(chapterNum) + "." + str(name) + ".py"
        f = open(path, "x")
        f.close()


print("Complete")