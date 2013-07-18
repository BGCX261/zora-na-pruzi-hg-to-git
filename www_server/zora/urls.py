import sys
import regex as re
sys.modules['re'] = re

from django.conf.urls import patterns, url,  include
#from zora.dispečer import url,  include


from django.views.generic import TemplateView

#from django.contrib import admin
#admin.autodiscover()
from zora.admin import urls as admin_urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zora.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin_urls)),
#    url(r'^time/$', 'pruga.views.current_time'),
    
    #    url(r'^$', 'app.views.index', name='index'),
#    když to napíšu takto,  nemusím psát view
    url(r'^$', TemplateView.as_view(template_name='index.html'),  name = 'home'),
    
#    url(r'^firmy$', 'zora.firma.seznam_firem'),
    url(r'^firma/ičo/(?P<ičo>\d+)/$', 'pruga.gdb.firma.najdi_firmu',  {'ičo': 45},  name = 'najdi_firmu'),
    url(r'^info/$', 'pruga.gdb.firma.info'),
    
)

#class Router(list):
#    
#    routy = {}
#    
#    def __init__(self,  *args):
#        for routa in args:
#            seznam = self.routy.setdefault(len(routa),  [])
#            seznam.append(routa)
#    
#    def parsuj(self,  cesta,  metoda = 'GET'):
##        cesta = cesta.encode('latin1').decode('utf8')
#        cesta = cesta.strip('/').split('/')
#        
#        délka = len(cesta)
#        
#        print(cesta,  délka)
#        
#        for routa in self.routy.get(délka,  []):
#            print(routa)
#            yield routa.parsuj(cesta)
##            if naparsováno is not None:
##                return naparsováno
#    
#def routa(*args):
#    return args
#  
#def číslo(hodnota):
#    pass
#
#urlpatterns__ = Router(
#               routa(), 
#               routa('firma',  'ičo',  číslo), 
#               )

#import sys
#import regex as re
#sys.modules['re'] = re
#
#from django.conf.urls import patterns, include, url
#
#from django.views.generic import TemplateView
#
#from django.contrib import admin
#admin.autodiscover()
#
#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'www.views.home', name='home'),
#    # url(r'^blog/', include('blog.urls')),
#
##    url(r'^$', 'app.views.index', name='index'),
##    když to napíšu takto,  nemusím psát view
#    url(r'^$', TemplateView.as_view(template_name='index.html')),
#    
#    url(r'^firmy$', 'zora.firma.seznam_firem'),
#    url(r'^firma/ičo/(?P<ičo>\d+)/$', 'zora.firma.najdi_firmu',  {'dotaz': 'najdi_firmu'}),
#    
#    url(r'^admin/', include(admin.site.urls)),
#)


