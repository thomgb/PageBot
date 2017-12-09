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
#     googleappsview.py
#
#     TO BE DEVELOPED: Live server using GoogleAppsContext to generate live pages.
#
import os
import shutil

from pagebot.elements.views.htmlview import HtmlView

class GoogleAppsView(HtmlView):
    u"""The GoogleAppsView implements a live Python server.
    For this PageBot + HtmlContext + FlatContext are deplyed and are running as 
    live server generating HTML/CSS pages. Similar to Xierpa3.
    
    This is different from the GoogleCloudView, which works similar to MampView 
    (local server) and GitView (gitub/docs server), serving locally saved static 
    HTML/CSS/JS file, that are created by the WebSite publications class, using 
    the HtmlContext as HTML/CSS generator.
    """
    viewId = 'GoogleApps'

