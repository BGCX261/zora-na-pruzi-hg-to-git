from mako.template import Template
from mako.lookup import TemplateLookup
import os

hen = os.path.dirname(__file__)
mylookup = TemplateLookup(directories=[hen], module_directory=hen,  input_encoding = 'utf-8')
#output_encoding='utf-8', encoding_errors='replace'


def url(jméno_routy,  *args,  **kwargs):
    from django.core.urlresolvers import reverse
    
    url = reverse(jméno_routy,  None,  args,  kwargs,  None,  None)
    return url

#    url = 'url do {}'.format(str(kwargs))
#    return url

def renderuj(jméno_šablony, **kwargs):
    mytemplate = mylookup.get_template(jméno_šablony)
    return mytemplate.render(url = url,  **kwargs)

