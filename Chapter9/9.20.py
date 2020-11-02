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


t = turtle.Turtle()
drawLS(t, "F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F",60,20)