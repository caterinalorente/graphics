import requests, os, re
from PIL import Image, ImageDraw
from StringIO import StringIO

def downloadImageFromWeb(coordX, coordY, labels):
    # open the web page picture and read it into a variable
    url = "http://imgs.xkcd.com/clickdrag/"
    imageName = str(coordX) + labels[0] + str(coordY) + labels[1] + ".png"
    url = url + imageName 

    r = requests.get(url)
    print r.status_code, imageName
    if r.status_code == 200: 
        image = Image.open(StringIO(r.content))
    else:
        if labels[0] == "n":
            image = Image.new("RGB", (2048, 2048), "white")
        else:
            image = Image.new("RGB", (2048, 2048), "black")
            
    image.save("xkcd/" + imageName)

def loopThroughCoordinates():     
    for n in range(1, 15):
        for e in range(1, 49):
            downloadImageFromWeb(n, e, labels=["n", "e"])   
        print "-----Done"
                    
    for n in range(1, 15):
        for w in range(1, 34):
            downloadImageFromWeb(n, w, labels=["n", "w"])
        print "-----Done n-w"        
                    
    for s in range(1, 26):
        for e in range(1, 49):
            downloadImageFromWeb(s, e, labels=["s", "e"])
        print "-----Done s-e"
                
    for s in range(1, 26):    
        for w in range(1, 34):
            downloadImageFromWeb(s, w, labels=["s", "w"])
        print "-----Done s-w"

def resizeDownloadedImages(imageSize):
    for image in os.listdir("xkcd/"):
        img = Image.open("xkcd/" + image)
        wpercent = (imageSize / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        
        img = img.resize((imageSize, hsize), Image.ANTIALIAS)
        print "Resizing ", image
        img.save("resized/" + image)
              
def putImagesTogether(size, width, height, imageSize):
    canvasSize = width*imageSize, height*imageSize
    canvas = Image.new("RGB", canvasSize, "white")
    centerY, centerX = [size[0]*imageSize, size[3]*imageSize]

    for image in os.listdir("resized/"):  
        im = Image.open("resized/" + image)
        x,y = translateCoords(centerX, centerY, image, imageSize);
        canvas.paste(im, (x,y))   
    canvas.show()   
    canvas.save("xkcd.png")

def translateCoords(canvasCenterX, canvasCenterY, imageName, imageSize):
    match = re.search("(\d\d?)(n|s)(\d\d?)(e|w)", imageName)
    yCoord = int(match.group(1))
    southNorth = match.group(2)
    xCoord = int(match.group(3))
    eastWest = match.group(4)

    if southNorth == "s": 
        y = canvasCenterY + ((yCoord-1) * imageSize)
    else:
        y = canvasCenterY + (yCoord * (-imageSize))
    
    if eastWest == "e":
        x = canvasCenterX + ((xCoord-1) * imageSize)
    else:
        x = canvasCenterX + (xCoord * (-imageSize))
        
    return x,y

def main():
    # ------------n-------------
    #|            |             |
    #|            |             |
    #|            |             |
    #w------------X-------------e
    #|            |             |
    #|            |             |
    #|            |             |
    # ------------s-------------|
    # x =1n1e
    
    size = [14, 48, 25, 33] #north, east, south, west
    width, height = size[1]+size[3], size[0]+size[2]
    imageSize = 250
    
#    loopThroughCoordinates()
    resizeDownloadedImages(imageSize)
    putImagesTogether(size, width, height, imageSize)
    
#main()        
img = Image.open("xkcd250.png")
img.show()
