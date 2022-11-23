from django.shortcuts import render, HttpResponse

# Create your views here.

layaut = """
            <h1>
                Proyecto web (LP3) | Elberth Antonio
            </h1>
            <hr/>
            <ul>
                <li>
                    <a href = "/inicio">Inicio</a>
                </li>
                <li>
                    <a href = "/saludo">Mensaje de Saludo</a>
                </li>
                <li>
                    <a href = "/rango">Mostrar Numeros [a,b]: </a>
                </li>
                <li>
                    <a href = "/rango2/10/15">Mostrar Numeros establecidos</a>
                </li>
            </ul>
            <hr/>
         """

def index(request):
    mensaje = """
                <h1>Inicio</h1>
                <button href = "saludo" = "saludo">Mensaje</button>
              """
    return HttpResponse(layaut+mensaje)

def saludo(request):
    mensaje = """

                <a><center>BIENVENIDOS AL CURSO</center></a>
                <table align="center">
                    <tr>
                        <th>
                            hola
                        </th>
                    </tr>
                    <tr>
                        <th>
                            <h1>Elberth Luque</h1>  
                        </th>
                    </tr>
                </table>

              """
    return HttpResponse (layaut + mensaje)

def rango(request):
    a = 10
    b = 20
    resultado = f"""
                    <h2>
                        Numeros de [{a}, {b}]
                    </h2>
                    resultado: <br>
                    <ul>    
                    """
    while a <= b:
        resultado += f"""<li>{a}</li>"""
        a+=1
    resultado += "</ul"
    return HttpResponse(layaut + resultado)

def rango2(request, a, b):

    
    resultado = f"""
                    <h2>
                        Numeros de [{a}, {b}]
                    </h2>
                    resultado: <br>
                    <ul>    
                    """
    while a <= b:
        resultado += f"""<li>{a}</li>"""
        a+=1
    resultado += "</ul"
    return HttpResponse(layaut + resultado)