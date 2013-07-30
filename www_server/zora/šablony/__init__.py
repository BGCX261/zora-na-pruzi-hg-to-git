from mako.template import Template
from mako.lookup import TemplateLookup
import os

hen = os.path.dirname(__file__)
mylookup = TemplateLookup(directories=[hen], module_directory=hen,  input_encoding = 'utf-8')
#output_encoding='utf-8', encoding_errors='replace'

from zora.dispečer import url,  url_souboru

def renderuj(jméno_šablony, **kwargs):
    mytemplate = mylookup.get_template(jméno_šablony)
    return mytemplate.render(url = url,  url_souboru = url_souboru,  **kwargs)

