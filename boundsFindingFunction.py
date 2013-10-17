from myro import *

def getLetterBounds():

    pic = makePicture("forCaptchaTest.jpg")

    width = getWidth(pic)
    height = getHeight(pic)
    print width
    print height
    normalPix = getPixel(pic, 0, height/2)
    normalRed = getRed(normalPix)
    print "normal " + str(normalRed)
    normalGreen = getGreen(normalPix)
    normalBlue = getBlue(normalPix)

    letterBounds = [0]
    counter = 0

    letterFound = False

    xCounter = 1
    yCounter = 1

    while(xCounter < width - 1):
        pix = getPixel(pic, xCounter, yCounter)
        #print xCounter
        #print yCounter
        XCoord = getX(pix)
        YCoord = getY(pix)
        pixRed = getRed(pix)
        #print pixRed
        pixGreen = getGreen(pix)
        pixBlue = getBlue(pix)

        bottomPix = getPixel(pic, xCounter, yCounter - 1)
        bottomXCoord = getX(bottomPix)
        bottomYCoord = getY(bottomPix)
        bottomPixRed = getRed(bottomPix)
        bottomPixGreen = getGreen(bottomPix)
        bottomPixBlue = getBlue(bottomPix)

        topPix = getPixel(pic, xCounter, yCounter + 1)
        topXCoord = getX(topPix)
        topYCoord = getY(topPix)
        topPixRed = getRed(topPix)
        topPixGreen = getGreen(topPix)
        topPixBlue = getBlue(topPix)

        rightPix = getPixel(pic, xCounter, yCounter)
        rightXCoord = getX(rightPix)
        rightYCoord = getY(rightPix)
        rightPixRed = getRed(rightPix)
        rightPixGreen = getGreen(rightPix)
        rightPixBlue = getBlue(rightPix)


        if(letterFound == True and (bottomPixRed + 10 >= normalRed or bottomPixRed - 10 <= normalRed) and (topPixRed + 10 >= normalRed or topPixRed - 10 <= normalRed) and (rightPixRed + 10 >= normalRed and rightPixRed == normalRed - 10)):
            letterBounds.insert(counter, xCounter)
            xCounter = xCounter + 1
            counter = counter + 1
            yCounter = 0
            letterFound = False
           

        

        if(pixRed != normalRed and pixGreen != normalGreen and pixBlue != normalBlue and letterFound == False):
            letterBounds.insert(counter, xCounter)
            counter = counter + 1
            xCounter = xCounter + 1
            yCounter = 0
            letterFound = True


        yCounter = yCounter + 1
            
        if(yCounter == height - 1 and xCounter < width - 1):
            yCounter = 1
            xCounter = xCounter + 1



    return letterBounds
            
        
    
            # a b c d e f g h i j k l m n o p q r s t u v w x y z
