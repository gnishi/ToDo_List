from django.db import models

#Check: Mejora: Que revise si los puntos son positivos.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puntos =  models.IntegerField()  

class Tareas(models.Model):
    nombre = models.CharField(max_length=50)
    detalle = models.CharField(max_length=50)
    puntos =  models.IntegerField()

class Premios(models.Model):
    premio = models.CharField(max_length=50)
    detalle = models.CharField(max_length=50)
    stock =  models.IntegerField()
    puntos =  models.IntegerField()

