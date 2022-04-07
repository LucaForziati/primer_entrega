from django.shortcuts import render

from .models import Astronauta
from .forms import Astronauta_formulario
# Create your views here.

def prueba_template(request):

    return render(request, "index.html")

def probando_padre(request):

    return render(request, "padre.html")

def iniciar(request):

    return render(request, "iniciar.html")

def crear_astronauta(request):

    if request.method == "POST":

        astronauta_formulario = Astronauta_formulario(request.POST)

        if astronauta_formulario.is_valid():

            astronauta_informacion = astronauta_formulario.cleaned_data
            
            astronauta = Astronauta (
                nombre = astronauta_informacion["nombre"],
                apellido = astronauta_informacion["apellido"],
                )
            astronauta.save()

            astronauta_contexto = astronauta_informacion

            return render(request, "astronauta_creado.html", {"astronauta_contexto": astronauta_contexto, "id" : astronauta.id})

    else: 

        astronauta_formulario = Astronauta_formulario()

        return render(request, "crear_astronauta.html", {"astronauta_formulario": astronauta_formulario})

