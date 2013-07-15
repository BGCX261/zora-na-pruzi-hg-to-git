from django.shortcuts import render

from datetime import datetime
from django.http import HttpResponse

def current_time(request):
    return HttpResponse(datetime.now().strftime('%H:%M:%S'))
