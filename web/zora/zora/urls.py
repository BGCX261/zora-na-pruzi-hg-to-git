import sys
import regex as re
sys.modules['re'] = re

from django.conf.urls import patterns, include, url


from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zora.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^time/$', 'pruga.views.current_time'),
    
    #    url(r'^$', 'app.views.index', name='index'),
#    když to napíšu takto,  nemusím psát view
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    
#    url(r'^firmy$', 'zora.firma.seznam_firem'),
    url(r'^firma/ičo/(?P<ičo>\d+)/$', 'pruga.gdb.firma.najdi_firmu',  {'ičo': 45}),
    url(r'^info/$', 'pruga.gdb.firma.info'),
    
)


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


