from django.conf.urls import patterns, include,  url
from zora.dispečer import davaj_pohled


urlpatterns = patterns('',
    
    url(r'^list/$', davaj_pohled(model = 'pruga.datagraf.server:davaj_seznam_databází',  pohled ='admin/seznam_databází'),  name = 'seznam_databází'),
    
    url(r'^create/(?P<jméno_databáze>\w+)/$', davaj_pohled(model = 'pruga.datagraf.server.davaj_seznam_databází',   pohled ='admin/vytvořím_databázi'),  name = 'vytvoř_databázi'),
    url(r'^start/(?P<jméno_databáze>\w+)/$', davaj_pohled(model = 'pruga.gdb.firma.najdi_firmu'),  name = 'spustím_databázi'),
    url(r'^stop/(?P<jméno_databáze>\w+)/$', davaj_pohled(model = 'pruga.gdb.firma.najdi_firmu'),  name = 'zastavím_databázi'),
    url(r'^status/(?P<jméno_databáze>\w+)/$', davaj_pohled(model = 'pruga.gdb.firma.najdi_firmu'),  name = 'stav_databáze'),
   
    
)
