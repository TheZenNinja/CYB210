import turtle

def DrawRect(myTurtle, sideLength):
    myTurtle.forward(sideLength * 2)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength * 2)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)

t = turtle.Turtle();
DrawRect(t, 100)