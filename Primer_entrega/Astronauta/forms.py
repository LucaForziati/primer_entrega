from django import forms

class Astronauta_formulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()

class Peso_luna_formulario(forms.Form):

    peso = forms.FloatField()

class Peso_marte_formulario(forms.Form):

    peso = forms.FloatField()

class Vel_luz_formulario(forms.Form):

    distancia = forms.FloatField()