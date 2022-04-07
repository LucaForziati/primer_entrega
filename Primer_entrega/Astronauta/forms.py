from django import forms

class Astronauta(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()

class Peso_luna(forms.Form):

    peso = forms.FloatField()

class Peso_marte(forms.Form):

    peso = forms.FloatField()

class Vel_luz(forms.Form):

    distancia = forms.IntegerField()