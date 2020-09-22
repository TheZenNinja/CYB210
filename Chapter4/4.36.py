import turtle

def frequencyChart(alist):
 
    countdict = {}

    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1

    itemlist = list (countdict.keys())
    minitem = 0
    maxitem = len(itemlist)-1

    countlist = countdict.values()
    maxcount = max(countlist)

    wn = turtle.Screen()
    chartT = turtle.Turtle()
    wn.setworldcoordinates(-1,-1,maxitem+1,maxcount+1)
    chartT.hideturtle()
    chartT.speed(10)
    
    barWidth = 0.25

    chartT.up()
    chartT.goto(-barWidth/2,0)
    chartT.down()
    chartT.goto(maxitem+barWidth/2,0)
    chartT.up()
    
    chartT.goto(-1,0)
    chartT.write("0",font =("Helvetica", 16,"bold"))
    chartT.goto(-1,maxcount)
    chartT.write(str(maxcount), font =("Helvetica",16,"bold"))
    
    for index in range(len(itemlist)):
        chartT.goto(index, -1)
        chartT.write(str(itemlist [index]), font =("Helvetica",16,"bold"))

        #drawing a square
        chartT.fillcolor("blue")
        chartT.goto(index - barWidth/2,0)
        chartT.down()
        chartT.begin_fill()
        chartT.goto(index - barWidth/2, countdict [itemlist [index]])
        chartT.goto(index + barWidth/2, countdict [itemlist [index]])
        chartT.goto(index + barWidth/2, 0)
        chartT.end_fill()
        chartT.up()

    wn.exitonclick()

data = [3, 3, 5, 7, 1, 2, 5, 2, 3, 4, 6, 3, 4, 6, 3, 4, 5, 6, 6]
frequencyChart(data);