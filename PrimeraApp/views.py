from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def display(request):
    return HttpResponse("<h1>Hola Mundo!</h1> <br> <p>HOLAAAA</>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b> Fecha y Hora Actual: </b>" + str(dt)
    return HttpResponse(s)