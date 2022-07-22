from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#El request es un parametreo que necesita django para manipular el peticion-respuesta (GET, POST, DELETE)

def saludo(request):    
    return HttpResponse(f"<a href='http://127.0.0.1:8000/territorio/saludo/sebasgg'>Enviar a saludo especial</a>")

def saludoEspecial(request, dato):
    return HttpResponse(f"Probando ando DJango... by: <strong style='color: blue;'> {dato} </strong>")

def calculadora(request, ope, num1, num2):

    if ope == 1:
        return HttpResponse(f"La suma de: <br/> {num1} + {num2} = <span style='color: red;'>{num1 + num2}</span>")
    elif ope == 2:
        return HttpResponse(f"La resta de: <br/> {num1} - {num2} = <span style='color: red;'>{num1 - num2}</span>")
    elif ope == 3: 
        return HttpResponse(f"La multiplicación de: <br/> {num1} * {num2} = <span style='color: red;'>{num1 * num2}</span>")
    else:
        return HttpResponse(f"La división de: <br/> {num1} / {num2} = <span style='color: red;'>{num1 / num2}</span>")


def inicio(request):
    return render(request, 'territorio/index.html')    

def loginForm(request):
    return render(request, 'territorio/login/login.html')

def login(request):

    u = request.POST["usuario"]
    c = request.POST["clave"]

    if u == "admin" and c == "sebas123":
        return HttpResponse("Bienvenido!!!") 
    return HttpResponse("Usuario o clave incorrectos...")