import turtle

def removeMatches(text, toRemove):
    newTxt = ""
    for l in text:
        if l not in toRemove:
            newTxt += l;
    return newTxt

def createNeighborDict(text):
    mainDict = {}
    text = text.lower()
    nonLetters = removeMatches(text, "abcdefghijklmnopqrstuvwxyz")
    letters = removeMatches(text, nonLetters)

    for i in range(1, len(letters)):
        letterDict = mainDict.setdefault(letters[i], {})
        maybeAdd(letters[i-1], letterDict)

        letterDict = mainDict.setdefault(letters[i-1], {})
        maybeAdd(letters[i], letterDict)
    return mainDict
def maybeAdd(ch, toDict):
    if ch in 'abcdefghijklmnopqrstuvwxyz':
        toDict[ch] = toDict.setdefault(ch, 0) + 1

def plotFrequencyChart(dict, letters):
    letters = letters.lower()

    alphabet = 'abcdefghijklmnopqrstuvwxyz';
    colors = ["blue", "red", "green", "purple", "orange", "yellow"]
    
    maxValue = 0

    for a in range(len(alphabet)):
        for l in range(len(letters)):
            if letters[l] in dict[alphabet[a]]:
                if alphabet[a] in dict:
                    if letters[l] in dict[alphabet[a]]:
                        data = dict[alphabet[a]][letters[l]];
                        if data > maxValue:
                            maxValue = data;

    numOfChunks = 26;
    chunkParts = len(letters);
    barWidth = 0.5;
    padding = 1;

    sizeX = numOfChunks * (chunkParts * barWidth + padding)
    sizeY = maxValue
    wn = turtle.Screen()
    t = turtle.Turtle()
    wn.setworldcoordinates(0,0, sizeX, sizeY)
    t.hideturtle()
    t.speed(10)

    #draw x axis
    t.up()
    t.goto(-barWidth/2,0)
    t.down()
    t.goto(sizeX-barWidth/2,0)
    t.up()
    
    #draw y axis
    t.up()
    t.goto(-barWidth/2,0)
    t.down()
    t.goto(-barWidth/2,sizeY)
    t.up()

    #y axis labels
    t.goto(-4, 0)
    t.write("0",font =("Helvetica", 16,"bold"))
    t.goto(-2, sizeY)
    t.write(sizeY, font =("Helvetica",16,"bold"))

    #Legend
    for l in range(len(letters)):
        t.goto(sizeX-sizeX/100, sizeY-sizeY/25*l)
        t.color(colors[l])
        t.write(letters[l], font =("Helvetica",16,"bold"))


    t.color("black")
    for a in range(len(alphabet)):
        rootPos = a * (chunkParts * barWidth + padding)
        t.goto(rootPos, -sizeY/25)
        t.write(alphabet[a], font =("Helvetica",16,"bold"))

        for l in range(len(letters)):
            pos = rootPos + barWidth * l;

            data = 0
            if alphabet[a] in dict:
                if letters[l] in dict[alphabet[a]]:
                    data = dict[alphabet[a]][letters[l]];

            #drawing a square
            t.fillcolor(colors[l])
            t.goto(pos - barWidth/2,0)
            t.down()
            t.begin_fill()
            t.goto(pos - barWidth/2, data)
            t.goto(pos + barWidth/2, data)
            t.goto(pos + barWidth/2, 0)
            t.end_fill()
            t.up()
    
    wn.exitonclick()

file = open("ch8-ciphertext.txt", "r")

neighborDict = createNeighborDict(file.read());

plotFrequencyChart(neighborDict, "aetn")

file.close()