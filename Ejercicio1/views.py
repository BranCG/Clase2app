from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mostrar_variable1(request):
    nombre = "Brandon"
    cachorro=0
    adulto=0
    senior=0
    try:
        cantidadPerrito = int(input('Ingrese la cantidad de perritos tiene la cosita: '))
        if cantidadPerrito<1:
            raise Exception('error')

        print(cantidadPerrito>0)
        while cantidadPerrito>0:
            try:
                cantidad=int(input('ingrese la edad 0 - 16 :'))
            
                if cantidad >=0 and cantidad <=16:
                    if cantidad <= 1:
                        cachorro+=1
                    elif cantidad >1 and cantidad <=5:
                        adulto+=1
                    elif cantidad > 6:
                        senior+=1
                else:
                    raise  Exception('error')
                cantidadPerrito=cantidadPerrito-1
            except ValueError:
                print('Error, ingresa solo valores numericos')    
            
    except:
        print('ERROR')   

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <h1>Hola {nombre}, Bienvenido a PatiPerrix </h1>
            <p>En este ejemplo, estamos generando el HTML directamente desde la vista</p>
            
            <p>Ejercicio 1</p>
            <table style="border:1px solid red;">
                <tr>
                    <th>Calificacion</th>
                    <th>Cantidad</th>
                </tr>
                <tr>
                    <td>Cachorros</td>
                    <td>{cachorro}</td>
                </tr>
                <tr>
                    <td>Adultos</td>
                    <td>{adulto}</td>
                </tr>
                <tr>
                    <td>senior</td>
                    <td>{senior}</td>
                </tr>
            </table>
        </body>
    </html>
    """
    
    return HttpResponse(html)