from django.contrib import admin
from django.urls import path
from .views import * # usuarioCrear, tareaCrear, premioCrear, tarea_listar

urlpatterns = [
    ### Ruta raiz.
    path('', inicio, name='Inicio'),    
    ### Crear Datos [por Url].
    path('agregar-usuario/', usuarioCrear, name='Crear-usuario'),
    path('agregar-tarea/',tareaCrear, name='Crear-tarea'),
    path('agregar-premio/', premioCrear, name='Crear-premio'),
    ### Ver Datos.
    path('lista-tarea/', tarea_listar, name='Listar-tarea'),
    path('rtado-tarea/', tarea_resultado, name='Rtdo-tarea'),
]

"""
path('agregar-usuario/<nombre>/<apellido>/<puntos>', usuarioCrear),
    path('agregar-tarea/<nombre>/<detalle>/<puntos>',tareaCrear),
    path('agregar-premio/<premio>/<detalle>/<stock>/<puntos>', premioCrear),
"""