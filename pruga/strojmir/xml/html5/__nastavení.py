#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>
    
from ..__nastavení import typemap

namespace = None
nsmap = None

def parser():
    '''
    HTMLParser(self,
                        encoding=None,
                        remove_blank_text=False,
                        remove_comments=False,
                        remove_pis=False,
                        strip_cdata=True,
                        no_network=True,
                        target=None,
                        XMLSchema schema=None,
                        recover=True,
                        compact=True
                        )
    '''
    
#    from lxml.html import  html5parser
#    return html5parser.HTMLParser()
    
    from lxml.etree import  HTMLParser
    return HTMLParser(
#                        remove_blank_text = True, 
#                        remove_comments = True 
                      )
