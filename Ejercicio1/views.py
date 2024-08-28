from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mostrar_variable1(request):
    nombre = str(input("Ingresa tu nombre: "))

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Hola {nombre}, Bienvenido a Back End </h1>
        <p>En este ejemplo, estamos generando el HTML directamente desde la vista</p>
    </body>
    </html>
    """
    
    return HttpResponse(html)