from django.db import models

# Create your models here.

class Astronauta(models.Model):

    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    peso_luna = models.FloatField(blank = True, null = True)
    peso_marte = models.FloatField(blank = True, null = True)
    distancia_recorrida = models.FloatField(blank = True, null = True)

class Peso_luna(models.Model):

    peso = models.FloatField()

class Peso_marte(models.Model):

    peso = models.FloatField()

class Vel_luz(models.Model):

    distancia = models.FloatField()