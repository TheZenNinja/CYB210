def CapitalizeFile(inputFile, outputFile):
    fileLines = []

    readFile = open(inputFile, "r")
    fileLines = readFile.readlines()
    readFile.close()

    writeFile = open(outputFile, "w")
    for l in fileLines:
        writeFile.write(l.upper())
    writeFile.close()
    
    print("Done")

CapitalizeFile("5.5 Input.txt", "5.5 Output.txt")