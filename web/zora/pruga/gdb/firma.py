from django.shortcuts import render, render_to_response

def najdi_firmu(request,  **kwargs):
#    x = {}
#    for klíč,  hodnota in kwargs:
#        klíč = klíč.strreplace()
#    
#    return render_to_response('firma.html',  {'ičo': kwargs})
    kw = str(kwargs)
    return HttpResponse('firma {}'.format(kw))
