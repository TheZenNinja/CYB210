import turtle

def drawLS(aTurtle, instructions, angle, distance):
    for cmd in instructions :
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        else :
            print('Error : %s is an unknown command '%cmd)

wn = turtle.Screen();
t = turtle.Turtle()
t.speed(10)
part = "F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F"
drawLS(t, part+"-"+part+"++"+part+"-"+part,60,10)
wn.exitonclick()