import turtle;
import random

def tree(t, trunkLength):
    if trunkLength < 5:
        return
    else :
        angle = random.randrange(15,45)
        
        t.forward(trunkLength)
        t.right(angle)
        tree (t, trunkLength -random.randrange(5,25))
        t.left (angle*2)
        tree (t, trunkLength -random.randrange(5,25))
        t.right (angle)
        t.backward (trunkLength)

wn = turtle.Screen();
t = turtle.Turtle()
t.speed(10)
#orientates and keeps the tree in frame
t.left(90)
t.up()
t.backward(150)
t.down()

tree(t,100)
wn.exitonclick()