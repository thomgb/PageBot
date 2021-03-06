# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#
#     Supporting usage of DrawBot, www.drawbot.com
#     Supporting usage of Flat, https://github.com/xxyxyz/flat
# -----------------------------------------------------------------------------
#
#     UseImageObjectFilters.py
#
#     This script generates page that show the behavior and working of the DrawBot
#     ImageObject filters.
#
from __future__ import division # Make integer division result in float.
import pagebot # Import to know the path of non-Python resources.

from pagebot import x2cx, y2cy
# Creation of the RootStyle (dictionary) with all available default style parameters filled.
from pagebot.style import getRootStyle, A4, CENTER, NO_COLOR,TOP, BOTTOM, MM
# Document is the main instance holding all information about the document togethers (pages, styles, etc.)

from pagebot.conditions import *
from pagebot.elements import *
from pagebot.document import Document
    
PagePadding = 64
PageSize = 500

GUTTER = 8 # Distance between the squares.
SQUARE = 10 * GUTTER # Size of the squares

FILTER_TYPES = {
}

# The standard PageBot function getRootStyle() answers a standard Python dictionary, 
# where all PageBot style entries are filled by their default values. The root style is kept in RS
# as reference for the ininitialization of all elements. 
# Each element uses the root style as copy and then modifies the values it needs. 
# Note that the use of style dictionaries is fully recursive in PageBot, implementing a cascading structure
# that is very similar to what happens in CSS.

# Export in _export folder that does not commit in Git. Force to export PDF.
EXPORT_PATH = '_export/UseImageElements.pdf' 

def makeDocument():
    u"""Make a new document."""

    #W = H = 120 # Get the standard a4 width and height in points.
    W = PageSize
    H = PageSize

    # Hard coded SQUARE and GUTTE, just for simple demo, instead of filling padding an columns in the root style.
    # Page size decides on the amount squares that is visible.
    # Page padding is centered then.
    sqx = int(W/(SQUARE + GUTTER)) # Whole amount of squares that fit on the page.
    sqy = int(H/(SQUARE + GUTTER))
    # Calculate centered paddings for the amount of fitting squares.
    # Set values in the rootStyle, so we can compare with column calculated square position and sizes.
    #rs['colH'] = rs['colW'] = SQUARE  # Make default colW and colH square.

    #padX = (W - sqx*(SQUARE + GUTTER) + GUTTER)/2
    my = (H - sqy*(SQUARE + GUTTER) + GUTTER)/2

    doc = Document(w=W, h=H, originTop=False, title='Color Squares', autoPages=1)
    
    view = doc.getView()
    view.padding = 0 # Aboid showing of crop marks, etc.
    view.showElementOrigin = True
    
    # Get list of pages with equal y, then equal x.    
    #page = doc[0][0] # Get the single page from te document.
    page = doc.getPage(0) # Get page on pageNumber, first in row (this is only one now).
    page.name = 'This is a demo page for floating child elements'
    page.padding = PagePadding
    
    page.gutter3D = GUTTER # Set all 3 gutters to same value

    im = newImage('images/cookbot10.jpg', (50, 50, 10), padding=0, parent=page, w=200, h=300,
        conditions=(Top2Top(), Fit2Width(), SolveBlock(), Shrink2BlockBottom()), 
        yAlign=BOTTOM, fill=(0, 1, 0, 0.3), stroke=(1, 0, 0)
    )
    # Give parent on creation, to have the css chain working.
    
    # Caption falls through the yr2 (with differnt z) and lands on yr1 by Float2BottomSide()    
    fs = doc.context.newString('Captions float below the image',
                               style=dict(font='Verdana',
                                          fontSize=20,
                                          textFill=1))
    cap = newTextBox(fs, name='Caption', parent=im, z=0,
        conditions=[ Fit2Width(), Float2Top()], 
        padding=4, font='Verdana', 
        yAlign=TOP, fontSize=9, textFill=1, strokeWidth=0.5, 
        fill=(0, 0, 1, 0.3), stroke=(0, 0, 1),
    )
    score = page.solve()
    if score.fails:
        print score.fails

    print im.h
    for e in im.elements:
        print e.h

    return doc # Answer the doc for further doing.
 
if __name__ == '__main__':


    Variable([
        #dict(name='ElementOrigin', ui='CheckBox', args=dict(value=False)),
         dict(name='PagePadding', ui='Slider', args=dict(minValue=10, value=30, maxValue=100)),
        dict(name='PageSize', ui='Slider', args=dict(minValue=100, value=400, maxValue=800)),
    ], globals())
           
    d = makeDocument()
    d.export(EXPORT_PATH) 

