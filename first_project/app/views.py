import datetime
import os
import pprint

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    pages = ['admin/',
             '',
             'current_time/',
             'workdir/']

    return HttpResponse(pages)


def show_current_time(request):
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')


def show_workdir(request):
    return HttpResponse(f'{os.listdir()}')
