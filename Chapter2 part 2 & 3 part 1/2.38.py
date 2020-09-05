import math

def isInCircle(x,y,radius):
    return (x**2 + y**2 <= radius**2)


print(isInCircle(1,1,1))