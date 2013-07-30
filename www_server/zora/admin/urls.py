from django.conf.urls import patterns, include,  url
from zora.dispečer import POHLED,  MODEL,  POST, FLASH


urlpatterns = patterns('',
    
    url(r'^list/$', MODEL(model = 'pruga.datagraf.server:davaj_jména_databází',  pohled ='admin/seznam_databází'),  name = 'seznam_databází'),
    
    url(r'^create/$', POHLED(pohled ='admin/vytvořím_databázi'),  name = 'vytvořím_databázi'),
    url(r'^create/vytvoř_databázi$', POST(model = 'pruga.datagraf.instalace:jakoby_instaluji',  redirect = 'vytvořil_jsem_databázi'),  name = 'vytvoř_databázi'),
    url(r'^vytvořil_jsem_databázi/$', FLASH(pohled ='admin/vytvořil_jsem_databázi'),  name = 'vytvořil_jsem_databázi'),
    
    url(r'^start/(?P<jméno_databáze>\w+)/$', MODEL(model = 'pruga.gdb.firma.najdi_firmu'),  name = 'spustím_databázi'),
    url(r'^stop/(?P<jméno_databáze>\w+)/$', MODEL(model = 'pruga.gdb.firma.najdi_firmu'),  name = 'zastavím_databázi'),
    url(r'^status/(?P<jméno_databáze>\w+)/$', MODEL(model = 'pruga.gdb.firma.najdi_firmu'),  name = 'stav_databáze'),
   
    
)
