from cImage import *
import random as rnd

window = ImageWin("Line Img",300,300)
lineImg = EmptyImage(300,300)
for i in range(300):
    lineImg.setPixel(i,i,Pixel(rnd.randrange(0,255),rnd.randrange(0,255),rnd.randrange(0,255)))
lineImg.draw(window)
lineImg.save("LineImage.gif")