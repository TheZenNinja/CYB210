from cImage import *

def  removeAllRed (imageFile):
     myimagewindow = ImageWin ("Image Processing", 600, 200)
     oldimage = FileImage (imageFile)
     oldimage.draw (myimagewindow)

     width = oldimage.getWidth ()
     height = oldimage.getHeight ()
     newim = EmptyImage (width, height)

     for y in range (height):
         for x in range (width):
             originalPixel = oldimage.getPixel (x, y)
             newPixel = Pixel(0,originalPixel.getGreen(), originalPixel.getBlue())
             newim.setPixel (x, y, newPixel)

     newim.setPosition (width +1, 0)
     newim.draw (myimagewindow)
     myimagewindow.exitOnClick()

removeAllRed("mickey.gif")