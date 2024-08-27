from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hola2(request):
    return HttpResponse("<h1>Segunda App!</h1>")