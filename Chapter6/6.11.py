from cImage import *

def blackAndWhitePixel(oldpixel):
    intensitySum = oldpixel.getRed() + oldpixel.getGreen() + oldpixel.getBlue()
    
    aveRGB = intensitySum // 3

    newPixel = Pixel(255,255,255)

    if aveRGB < 200:
       newPixel = Pixel(0, 0, 0)

    return newPixel

def makeBlackAndWhite(imageFile):
    myimagewindow = ImageWin("Image Processing", 600, 200)
    oldimage = FileImage(imageFile)
    oldimage.draw(myimagewindow)

    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = EmptyImage(width, height)

    for y in range(height):
        for x in range(width):
            originalPixel = oldimage.getPixel(x, y)
            newPixel = blackAndWhitePixel(originalPixel)
            newim.setPixel(x, y, newPixel)

    newim.setPosition(width +1, 0)
    newim.draw(myimagewindow)
    myimagewindow.exitOnClick()

makeBlackAndWhite("mickey.gif")