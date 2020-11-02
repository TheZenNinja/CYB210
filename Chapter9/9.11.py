import turtle;
import random

def tree(t, trunkLength):
    if trunkLength < 5:
        return
    else :
        angle = random.randrange(15,45)
        t.forward(trunkLength)
        t.right(angle)
        tree (t, trunkLength -15)
        t.left (angle*2)
        tree (t, trunkLength -15)
        t.right (angle)
        t.backward (trunkLength)

wn = turtle.Screen();
t = turtle.Turtle()
t.speed(10)
t.left(90)
tree(t,100)
wn.exitonclick()