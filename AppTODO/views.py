from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Usuarios, Tareas, Premios
from .forms import FormCrearUsuario, FormCrearTarea, FormCrearPremio
#Check: Mejoras: Incluir un ERROR HANDLING.
#Check: Mejoras: Buscador de Info - Sume puntos.


########### VIEW DE INICIO
def inicio(req):
    return render(req, "inicio.html")


########### VIEW DE CREACION
def usuarioCrear(req):
    #Ver si viene como GET [Url] o POST [Form]
    print('method', req.method)
    print('POST', req.POST)
    
    if req.method == 'POST':
        miFormulario = FormCrearUsuario(req.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = Usuarios(nombre=data['nombre'], apellido=data['apellido'], puntos=data['puntos'])
            usuario.save()
            
            return render(req, "inicio.html")
    
    else:
        miFormulario = FormCrearUsuario()
        return render(req, "usuarioCrear.html", {"miFormulario": miFormulario})

def tareaCrear(req):
    if req.method == 'POST':
        miFormulario = FormCrearTarea(req.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            tarea = Tareas(nombre=data['nombre'], detalle=data['detalle'], puntos=data['puntos'])
            tarea.save()
            
            return render(req, "inicio.html")
    
    else:
        miFormulario = FormCrearTarea()
        return render(req, "tareaCrear.html", {"miFormulario": miFormulario})

def premioCrear(req):
    if req.method == 'POST':
        miFormulario = FormCrearPremio(req.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            premio = Premios(premio=data['premio'], detalle=data['detalle'], stock=data['stock'], puntos=data['puntos'])
            premio.save()
            
            return render(req, "inicio.html")
    
    else:
        miFormulario = FormCrearPremio()
        return render(req, "premioCrear.html", {"miFormulario": miFormulario})


### VIEW DE CONSULTAS
def tarea_listar(req):    
    lista = Tareas.objects.all()
    return render(req, "lista_tareas.html", {"lista_tareas": lista})

def tarea_resultado(req: HttpRequest):
    print('TAREA RTDO 1', req.GET)
    print('TAREA RTDO 2', req.GET["puntos"])
    if req.GET["puntos"]:
        puntos = req.GET["puntos"]
        DbTarea = Tareas.objects.filter(puntos__gte=puntos)
        """
            # Para Testear el resultado
            print('TAREA A', puntos)
            print('TAREA B', DbTarea)
            print('TAREA C', Tareas.objects.all())
            print('TAREA D', len(DbTarea))
        """
        if len(DbTarea) >0:
            return render(req, "rtdo_tareas.html", {"puntaje_buscado": puntos, "puntaje_resultado": DbTarea})
        else:
            DbTarea = "nada"
            return render(req, "rtdo_tareas.html", {"puntaje_buscado": puntos, "puntaje_resultado": DbTarea})
    else:
            respuesta = "Debe mejorar su busqueda"
    
    return HttpResponse(respuesta)