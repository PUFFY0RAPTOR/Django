from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aprendiz, Monitoria, Actividades
from django.urls import reverse

# Create your views here.

#El request es un parametro que necesita django para manipular el peticion-respuesta (GET, POST, DELETE)

def index(request):    
    return render(request, 'territorio/index.html')

def listarAprendiz(request):

    q = Aprendiz.objects.all()
    contexto = { 'datos': q }

    return render(request, 'territorio/aprendiz/listar_aprendiz.html', contexto)

def aprendicesFormulario(request):
    return render(request, 'territorio/aprendiz/crear_aprendiz.html')

def aprendicesGuardar(request):
    try:
        q = Aprendiz(
            cedula = request.POST["cedula"],
            nombre = request.POST["nombre"],
            apellido = request.POST["apellido"],
            fecha_nacimiento = request.POST["fecha_nacimiento"],
        )
        q.save()
        #return HttpResponse("Aprendiz guardado correctamente<br/><a href='../aprendices/'>Listar aprendices</a>")
        return HttpResponseRedirect(reverse('territorio:aprendices'))
    except Exception as e:
        return HttpResponse("Error : " + str(e))

def listarMonitorias(request):

    m = Monitoria.objects.all()

    contexto = { 'datos': m}

    return render(request, 'territorio/monitoria/listar_monitoria.html', contexto)

def monitoriaFormulario(request):

    q = Aprendiz.objects.all()

    #s = Monitoria.objects.get()

    contexto = { 'data': q}

    return render(request, 'territorio/monitoria/crear_monitoria.html', contexto)

def monitoriaGuardar(request):
    
    f = int(request.POST["aprendiz"])
    
    try:
        q = Monitoria(
            cat = request.POST["cat"],
            aprendiz = Aprendiz.objects.get(pk = f),
            fecha_inicio = request.POST["fecha_inicio"],
            fecha_final = request.POST["fecha_final"],
        )
        q.save()
        return HttpResponseRedirect(reverse('territorio:monitorias'))

    except Exception as e:
        return HttpResponse("Error : " + str(e))

def listarActividades(request):

    a = Actividades.objects.all()
    contexto = {'datos': a}

    return render(request, 'territorio/actividades/listar_actividades.html', contexto)
