import turtle;
import random;
def showMontePi(resolution):
    scr = turtle.Screen()
    drawing = turtle.Turtle()
    
    scr.setworldcoordinates(-2,-2,2,2)
    
    drawing.speed(10)
    
    drawing.up()
    drawing.goto(-1,0)
    drawing.down()
    drawing.goto(1,0)
    
    drawing.up()
    drawing.goto(0,1)
    drawing.down()
    drawing.goto(0,-1)
    
    total = 0
    drawing.up()
    
    for i in range(resolution):
        x = random.random()*2-1
        y = random.random()*2-1
        
        #due to working with a radius of 1, taking the sqrt would be redundant
        sqrDist = x**2 + y**2
        
        drawing.goto(x,y);
        if sqrDist <= 1:
            total += 1
            drawing.color("blue")
        else:
            drawing.color("red")
    
        drawing.dot();
    
    pi = total/resolution * 4
    drawing.hideturtle()
    scr.exitonclick();
    return pi;

print(showMontePi(1000))