from django.shortcuts import render, render_to_response

from django.http import HttpResponse

def najdi_firmu(request,  ičo,  **kwargs):
    x = {}
    for klíč,  hodnota in kwargs:
        klíč = klíč.strreplace()
    
    return render_to_response('firma.html',  {'ičo': ičo})
#    kw = str(kwargs)
#    return HttpResponse('firma {}'.format(kw))

def info(request,  **kwargs):
    kw = str(kwargs)
    
    meta = []
    for klíč,  hodnota in request.META.items():
        meta.append('<dt>{}</dt><dl>{}</dl>'.format(klíč,  hodnota))
        
    meta = '<dl>{}</dl>'.format('\n'.join(meta))
    
    return HttpResponse('''
    firma bere {} request.path {} <h2>{} </h2><h2>META </h2>{}'
    '''.format(
                                                               kw, 
                                                               request.path,  
                                                               request.build_absolute_uri(), 
                                                               meta
                                                               ))
    
