import datetime

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):

    return  HttpResponse()

def show_current_time(request):

    return HttpResponse(f'Time = {datetime.datetime.now().time()}')

def show_workdir(request):
    return HttpResponse('Привет, наша первая страница')