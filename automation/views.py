import json
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .lib.scheduler import sch
from .lib.sun import *
from .lib.context import Context
from .lib.execution_element import ExecutionElement

def index(request):
    return render(request, 'index1.html', get_data())

def status(request):
    return JsonResponse(get_data(), safe=False)

def isday(request):
    return JsonResponse(sch.IsDay, safe=False)

def get_data():
    return {
        'ExecutionElements': json.loads(str(sch.context)),
        'Now': Sun.Now().strftime('%H:%m:%S'),
        'IsDay': sch.IsDay,
        'Dawn': Sun.Dawn().strftime('%H:%m:%S'),
        'Sunrise': Sun.Sunrise().strftime('%H:%m:%S'),
        'Noon': Sun.Noon().strftime('%H:%m:%S'),
        'Sunset': Sun.Sunset().strftime('%H:%m:%S'),
        'Dusk' : Sun.Dusk().strftime('%H:%m:%S')
        }