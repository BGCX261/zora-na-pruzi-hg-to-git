from django.shortcuts import render, render_to_response

#from django.http import HttpResponse

def najdi_firmu(request,  ičo,  **kwargs):
    x = {}
    for klíč,  hodnota in kwargs:
        klíč = klíč.strreplace()
    
    return render_to_response('firma.html',  {'ičo': ičo})
#    kw = str(kwargs)
#    return HttpResponse('firma {}'.format(kw))
