# -----------------------------------------------------------------------------
#     Copyright (c) 2016+ Type Network, www.typenetwork.com, www.pagebot.io
#
#     P A G E B O T
#
#     Licensed under MIT conditions
#     Made for usage in DrawBot, www.drawbot.com
# -----------------------------------------------------------------------------
#Z
#     UseTextFlows.py
#
from __future__ import division # Make integer division result in float.
import pagebot # Import to know the path of non-Python resources.

from pagebot import x2cx, y2cy
# Creation of the RootStyle (dictionary) with all available default style parameters filled.
from pagebot.style import getRootStyle, A4, CENTER, RIGHT, LEFT, NO_COLOR,TOP, BOTTOM, MM
# Document is the main instance holding all information about the document togethers (pages, styles, etc.)
from pagebot import getFormattedString

from pagebot.conditions import *
from pagebot.elements import *
from pagebot.document import Document

DoTextFlow = False   
PagePadding = 32
PageSize = 500

GUTTER = 8 # Distance between the squares.
SQUARE = 10 * GUTTER # Size of the squares

# The standard PageBot function getRootStyle() answers a standard Python dictionary, 
# where all PageBot style entries are filled by their default values. The root style is kept in RS
# as reference for the ininitialization of all elements. 
# Each element uses the root style as copy and then modifies the values it needs. 
# Note that the use of style dictionaries is fully recursive in PageBot, implementing a cascading structure
# that is very similar to what happens in CSS.

# Export in _export folder that does not commit in Git. Force to export PDF.
EXPORT_PATH = '_export/UseTextFlows.pdf' 

def makeDocument():
    u"""Make a new document."""

    #W = H = 120 # Get the standard a4 width and height in points.
    W = H = PageSize
    #W, H = A4
    # Hard coded SQUARE and GUTTE, just for simple demo, instead of filling padding an columns in the root style.
    # Page size decides on the amount squares that is visible.
    # Page padding is centered then.
    sqx = int(W/(SQUARE + GUTTER)) # Whole amount of squares that fit on the page.
    sqy = int(H/(SQUARE + GUTTER))
    # Calculate centered paddings for the amount of fitting squares.
    # Set values in the rootStyle, so we can compare with column calculated square position and sizes.
    my = (H - sqy*(SQUARE + GUTTER) + GUTTER)/2

    doc = Document(w=W, h=H, originTop=False, title='Text Flow', autoPages=1)
    
    view = doc.getView()
    view.padding = 40 # Aboid showing of crop marks, etc.
    view.showPageCropMarks = True
    view.showPageRegistrationMarks = True
    view.showPageFrame = True
    view.showElementOrigin = True
    view.showElementDimensions = False
    
    # Get list of pages with equal y, then equal x.    
    #page = doc[0][0] # Get the single page from te document.
    page = doc.getPage(0) # Get page on pageNumber, first in row (this is only one now).
    page.name = 'This is a demo page for floating child elements'
    page.padding = PagePadding
    
    page.gutter3D = GUTTER # Set all 3 gutters to same value

    if BoxWidths < 200:
        tColor = (1, 0, 0)
        
    else:
        tColor = (0, 0, 1)
    
    s = ''
    for n in range(10):
        s += '(%d) Volume of text defines the box height.\n' % (n+1)
    if DoTextFlow:
        h1 = 100
    else:
        h1 = None    
    e1 = newTextBox(s, 
        name='ElasticTextBox1', 
        parent=page, padding=4, x=100, w=BoxWidth, font='Verdana', h=h1, maxW=W-2*PagePadding,      
        conditions=[Left2Left(), Float2Top()], yAlign=BOTTOM, xAlign=LEFT,
        leading=5, fontSize=9, textFill=tColor, strokeWidth=0.5, fill=0.9, stroke=None,
    )
    print e1.mb
    e2 = newTextBox(s, 
        name='ElasticTextBox2', 
        parent=page, padding=4, x=100, w=BoxWidth, font='Verdana', maxW=W-2*PagePadding,
        conditions=[Right2Right(), Float2Top()], yAlign=TOP, leading=5, 
        fontSize=9, textFill=0.9, strokeWidth=0.5, fill=tColor, stroke=None,
    )
    print e2.mt, e2.mb, e2.getFloatTopSide(), e2.mTop, e2.top
    
    score = page.solve()
    if score.fails:
        print score.fails

    return doc # Answer the doc for further doing.
 
if __name__ == '__main__':


    Variable([
        #dict(name='ElementOrigin', ui='CheckBox', args=dict(value=False)),
         dict(name='DoTextFlow', ui='CheckBox', args=dict(value=False)),
         dict(name='BoxWidth', ui='Slider', args=dict(minValue=200, value=500, maxValue=PageSize)),
        dict(name='PagePadding', ui='Slider', args=dict(minValue=0, value=30, maxValue=100)),
        dict(name='PageSize', ui='Slider', args=dict(minValue=200, value=500, maxValue=PageSize)),
    ], globals())
           
    d = makeDocument()
    d.export(EXPORT_PATH) 
