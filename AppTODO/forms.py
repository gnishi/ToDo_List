from django import forms

#Check: Mejora: Que revise si los puntos son positivos.

class FormCrearUsuario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    puntos =  forms.IntegerField() #Check: Se puede hacer que inicie por DEFAULT con un valor?
    

class FormCrearTarea(forms.Form):
    nombre = forms.CharField(max_length=50)
    detalle = forms.CharField(max_length=50)
    puntos =  forms.IntegerField()
    
class FormCrearPremio(forms.Form):
    premio = forms.CharField(max_length=50)
    detalle = forms.CharField(max_length=50)
    stock =  forms.IntegerField()
    puntos =  forms.IntegerField()