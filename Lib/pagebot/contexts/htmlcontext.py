# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens & Font Bureau
#     www.pagebot.io
#     Licensed under MIT conditions
#     
#     Supporting usage of DrawBot, www.drawbot.com
#     Supporting usage of Flat, https://github.com/xxyxyz/flat
# -----------------------------------------------------------------------------
#
#     htmlcontext.py
#
from basecontext import BaseContext
from pagebot.contexts.builders import WebBuilder
from pagebot.contexts.strings. htmlstring import HtmlString, newHtmlString

class HtmlContext(BaseContext):
    u"""A HtmlContext instance combines the specific functions of the Flat library
    This way it way it hides e.g. the type of BabelString
    instance needed, and the type of HTML/CSS file structure to be created."""

    b = WebBuilder() # self.b builder for this canvas.
 
    @classmethod
    def newString(cls, s, view=None, e=None, style=None, w=None, h=None, fontSize=None, 
            styleName=None, tagName=None):
        u"""Create a new styles BabelString(HtmlString) instance from s, using e or style.
        Ignore and answer s if it is already a HtmlString."""
        if isinstance(s, basestring):
            s = newHtmlString(s, view=view, e=e, style=style, w=w, h=h, 
                fontSize=fontSize, styleName=styleName, tagName=tagName)
        assert isinstance(s, HtmlString)
        return s