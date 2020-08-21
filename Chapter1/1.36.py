import turtle

def drawSpiral(turtleA,turtleB,maxSide):
    for sideLength in range(0, maxSide+1, 5):
        turtleA.forward(sideLength)
        turtleB.backward(sideLength)
        turtleA.right(90)
        turtleB.right(90)

a = turtle.Turtle()
b = turtle.Turtle()

drawSpiral(a,b, 250)