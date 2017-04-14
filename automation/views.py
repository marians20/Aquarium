import json
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .lib.scheduler import sch
from .lib.sun import *
from .lib.context import Context
from .lib.execution_element import ExecutionElement
from .ajax import *

def index(request):
    return render(request, 'index1.html', get_data())
