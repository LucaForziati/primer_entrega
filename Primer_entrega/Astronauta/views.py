from django.http import HttpResponse
from django.shortcuts import render

from .models import Astronauta, Peso_luna, Peso_marte, Vel_luz
from .forms import Astronauta_formulario, Peso_luna_formulario, Peso_marte_formulario, Vel_luz_formulario
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

def luna(request):

    if request.method == "POST":

        luna_formulario = Peso_luna_formulario(request.POST)

        if luna_formulario.is_valid():

            luna_informacion = luna_formulario.cleaned_data
            
            luna = Peso_luna (
                peso = luna_informacion["peso"],  
                )
            luna.save()

            numero_astronauta = request.POST["numero_astronauta"]

            peso_luna = Astronauta.objects.get(id = int(numero_astronauta)) 
            peso_luna.peso_luna = (luna.peso / 9.81) * 1.62
            peso_luna.save()

            luna_contexto = luna_informacion

            return render(request, "tu_peso_luna.html", {"luna_contexto": luna_contexto, "peso_luna": peso_luna.peso_luna})

    else: 

        luna_formulario = Peso_luna_formulario()

        return render(request, "luna.html", {"luna_formulario": luna_formulario})

def marte(request):

    if request.method == "POST":

        marte_formulario = Peso_marte_formulario(request.POST)

        if marte_formulario.is_valid():

            marte_informacion = marte_formulario.cleaned_data
            
            marte = Peso_marte (
                peso = marte_informacion["peso"],  
                )
            marte.save()

            numero_astronauta = request.POST["numero_astronauta"]

            peso_marte = Astronauta.objects.get(id = int(numero_astronauta)) 
            peso_marte.peso_marte = (marte.peso * 3.72) / 9.80
            peso_marte.save()

            marte_contexto = marte_informacion

            return render(request, "tu_peso_marte.html", {"marte_contexto": marte_contexto, "peso_marte": peso_marte.peso_marte})

    else: 

        marte_formulario = Peso_marte_formulario()

        return render(request, "marte.html", {"marte_formulario": marte_formulario})

def velocidad_luz(request):

    if request.method == "POST":

        velocidad_formulario = Vel_luz_formulario(request.POST)

        if velocidad_formulario.is_valid():

            velocidad_informacion = velocidad_formulario.cleaned_data
            
            velocidad = Vel_luz (
                distancia = velocidad_informacion["distancia"],  
                )
            velocidad.save()


            numero_astronauta = request.POST["numero_astronauta"]

            velocidad_nave = Astronauta.objects.get(id = int(numero_astronauta)) 
            velocidad_nave.distancia_recorrida = float(velocidad.distancia/(299792.45*90/100))
            velocidad_nave.save()

            velocidad_contexto = velocidad_informacion

            return render(request, "velocidad_nave.html", {"velocidad_contexto": velocidad_contexto, "velocidad": velocidad_nave.distancia_recorrida})

    else: 
        velocidad_formulario = Vel_luz_formulario()
        
        return render(request, "velocidad.html", {"velocidad_formulario": velocidad_formulario})   


def buscar(request):

    if request.method == "POST":
        id_astronauta = request.POST["astronauta"]
        dato_astronauta = Astronauta.objects.get(id = id_astronauta)

        astronauta_contexto = dato_astronauta

        return render(request, "astronauta_perfil.html", {"astronauta_contexto": astronauta_contexto})
    else:
        
        return render(request, "busqueda_astronauta.html")
    

