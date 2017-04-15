import json
from django.http import JsonResponse
from .lib.scheduler import sch
from .lib.sun import *
from .lib.context import Context
from .lib.execution_element import ExecutionElement

def get_data():
    return {
        'ExecutionElements': json.loads(str(sch.context)),
        'Now': Sun.Now().strftime('%H:%M:%S'),
        'IsDay': sch.IsDay,
        'Dawn': Sun.Dawn().strftime('%H:%M:%S'),
        'Sunrise': Sun.Sunrise().strftime('%H:%M:%S'),
        'Noon': Sun.Noon().strftime('%H:%M:%S'),
        'Sunset': Sun.Sunset().strftime('%H:%M:%S'),
        'Dusk' : Sun.Dusk().strftime('%H:%M:%S')
        }

def status(request):
    return JsonResponse(get_data(), safe=False)

def isday(request):
    return JsonResponse(sch.IsDay, safe=False)

def set_execution_element(request, id, value):
    Id = int(id)
    if Id == 0:
        set_all_execution_elements(request, value)
    else:
        Value = int(value)
        sch.Context[Id].Overriden = True
        sch.Context[Id].OverridenValue = Value
    return JsonResponse(get_data(), safe=False)

def set_execution_element_auto(request, id):
    Id = int(id)
    if Id == 0:
        set_all_execution_elements_auto(request)
    else:
        sch.Context[Id].Overriden = False
    return JsonResponse(get_data(), safe=False)

def set_all_execution_elements(request, value):
    Value = int(value)
    for executionElement in sch.Context.ExecutionElements:
        executionElement.Overriden = True
        executionElement.OverridenValue = Value

def set_all_execution_elements_auto(request):
    for executionElement in sch.Context.ExecutionElements:
        executionElement.Overriden = False