from __future__ import division
import os # Python library that allows access to the OS file system.
from random import choice, shuffle

SHOW_FILTERED_AVAILABLE_FONTS = False
SHOW_GRID = True
AMOUNT_OF_SKETCHES = 5

def scaledImage(path, (x, y, w, h)):
    imageW, imageH = imageSize(path)
    save() # Save graphics state
    s = w/imageH
    scale(s)
    image(path, (x/s, y/s))
    restore() # Get back to original graphics state
    return w*s, y*s
    
def drawPoster(bgColor, textColor):    
    # Create the page
    newPage(W, H)
    # Fill background of whole page
    r, g, b = bgColor
    fill(r, g, b) # Set the "brush" color to the r(ed), g(reen), b(lue) value that we calculated.
    stroke(None)
    #stroke(1, 0, 0) # DEMO: outline color of the shape
    #strokeWidth(100) # DEMO: thickness of the outline
    rect(0, 0, W, H)
    #oval(0, 0, W, H) # Drawing an oval instead of a rect

    # Draw title on the poster (not do it this way as separate typographic values
    #titleSize = 128
    #fill(0)
    #font('Superclarendon-Bold')
    #fontSize(titleSize)
    #text('Asian food', (30, H-titleSize))

    # Draw title on the poster using FormattedString
    fontName = 'Superclarendon-Bold'
    fontNameItalic = 'Superclarendon-BoldItalic'
    captionFontName = 'Superclarendon-Regular'

    titleSize = 140
    fs = FormattedString('Asian', font=fontName, 
            fontSize=titleSize, fill=textColor, lineHeight=titleSize*1.1)
    fs += FormattedString(' food\n', font=fontNameItalic, 
            fontSize=titleSize, fill=textColor, lineHeight=titleSize*1.1)
    fs += FormattedString('All the pastas you ever need in your life.', font=fontNameItalic, fontSize=titleSize/3, fill=textColor)
 
    textWidth = W-ML-MR # Calculate the area on the post that can contain the title width.
    x, y = ML, H-titleSize*2 # Calculate the position of the title
    w, h = textSize(fs, width=textWidth) # Get the size of the text on this width.
    fill(0, 0, 0, 0.2) # Temporary fill the text box are with transparant black
    rect(x, y, w, h) # So we can see where it went to (if not showing text).
    textBox(fs, (x, y, min(w, textWidth), h )) # Draw the title in a box that fits the page.

    x = ML
    y = Y = H-800
    # Draw the images.
    imageFolder = 'images/'
    for fileName in os.listdir(imageFolder):
        if fileName.startswith('.'):
            continue
        if not fileName.endswith('jpg'):
            continue
        #x, y = random()*W, random()*H
        # Randomly shuffle the order of the Lorum Ipsum text pieces.
        shuffle(LORUM_IPSUMS)
        # Pick a random (2, 3, 4) pieces selection, starting at index 0 a
        LORUM_IPSUM = '\n'.join(LORUM_IPSUMS[:choice((2,3))])

        imageWidth = CW
        imageW, imageH = scaledImage(imageFolder + fileName, (x, y, imageWidth, 0))
        print imageFolder + fileName, x, y
        # Draw a nice transparant color on the bottom left of the image.
        fill(1, random(), 0, 0.5)
        cphm = 208# colorPhotoMarker
        cphm = max(100,cphm) # Never make square smaller than 100
        cphm = min(300,cphm) # Never make sqyare larger than 300
        rect(x-cphm/2, y-cphm/2, cphm, cphm)
        # Add a name to the type of pasta.
        captionText = CAPTION.get(fileName, 'Cannot find this caption') + '\n'
        captionSize = cphm/4
        fs = FormattedString(captionText, font=fontName, fontSize=captionSize, lineHeight=cphm/4,
            fill=textColor)
        fs += FormattedString(LORUM_IPSUM, font=captionFontName, fontSize=12, lineHeight=12*1.8,
            fill=textColor)
        textW, textH = textSize(fs, width=imageWidth) # Get the size of the text on this width.
    
        textBox(fs, (x, y-textH, textW, textH))

        y -= imageH/10 + textH + captionSize
        if y < 0:
            x += CW + G
            y = Y
    
    # Draw the grid lines
    for cx in range(int(COLUMNS)):
        stroke(0, 0, 1)
        strokeWidth(0.5)
        x = cx*(CW+G)+MR
        line((x, 0), (x, H))
        line((x+CW, 0), (x+CW, H))


def run():    
    #print installedFonts() # Print all font names installed in the system
    if SHOW_FILTERED_AVAILABLE_FONTS:
        for fontName in installedFonts():
            if 'clarendon' in fontName.lower():
                print fontName

    LORUM_IPSUMS = [
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce pretium ex lorem, quis volutpat mi mollis ac. Aliquam consequat orci nec tempus venenatis. """,
        """Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam quis purus consequat, lacinia tortor in, mattis diam. Suspendisse malesuada eleifend enim vel lacinia. """,
        """Maecenas pellentesque elit turpis, sed tincidunt lectus placerat eu. Etiam finibus mollis feugiat. Proin mattis lacus venenatis fringilla euismod. Morbi nunc erat, consequat in neque sit amet, posuere maximus purus.
        """,
        """Etiam posuere lacus a tincidunt hendrerit. In feugiat lorem tortor, non rhoncus velit finibus ut. Vivamus iaculis orci id viverra aliquet. Donec enim nibh, pellentesque sed condimentum in, vulputate ut massa. Nunc interdum metus sit amet dapibus sodales. Quisque sed quam ac est facilisis congue. Nulla aliquam condimentum nisi sit amet ultrices."""
    ]

    CAPTION = {
        'pasta1.jpg': 'Red sauce and cream',
        'pasta2.jpg': 'Pens and green',
        'pasta3.jpg': 'Pasta on the deck',
        'pasta4.jpg': 'Goulash or tortilla?',
        'pasta5.jpg': 'Pasta screws',
        'pasta6.jpg': 'Green pens',
        'pasta7.jpg': 'Noodles or pasta?'
    }
        
    MM = 72/25.4
    A0 = 841*MM, 1189*MM
    A1 = 594*MM, 841*MM
    A2 = 420*MM, 594*MM
    A3 = 297*MM, 420*MM
    A4 = 210*MM, 297*MM 
    A5 = 148*MM, 210*MM

    # Define the size of the poster
    W, H = A1
    W += 14
    #H, W = A1 # Use for landscape
    #W = 2*W # Make long banner
    ML = MR = 100 # Margin left and margin right
    G = MR/2 # Gutter, space between the columns

    # Fixed number of columns on a page width
    if 1:
        COLUMNS = 3
        CW = (W - ML - MR - G*(COLUMNS-1))/COLUMNS # Calculate space of 3 columns
    else: # Make columns size dependent on height
        CW = 1/6*H
        COLUMNS = (W-ML-MR)/(CW+G)

    # Define color of the background
    # Yelloq version
    for n in range(AMOUNT_OF_SKETCHES):
        if n == 0: # Force fixed color, yellow background               
            bgColor = 0xF5/256, 0xF5/256, 0xDC/256 #   #F5F5DC
            textColor = 0
        elif n == 1: # Force fixed color, black background
            bgColor = 0, 0, 0 # In case of black background
            textColor = (1, 1, 1) # Text red, text green, text blue
        else: # Random 
            yellowish = random()
            bgColor = yellowish, yellowish, yellowish*0.95
            tColor = 1-yellowish
            if abs(yellowish - tColor) < 0.3: # Difference in contrast too small, put text in white or black.
                if yellowish < 0.5:
                    tColor = 1
                else:
                    tColor = 0
            textColor = tColor, tColor, tColor
            
        drawPoster(bgColor, textColor)
 
if __name__ == '__main__':   
    run()  
    saveImage('_export/DB_FoodPosters.pdf')
    saveImage('_export/DB_FoodPosters.png', multipage=True) # Save images a separate PNG files.
    #saveImage('_export/DB_FoodPosters.gif')
