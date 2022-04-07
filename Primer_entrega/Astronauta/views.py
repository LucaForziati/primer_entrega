from django.shortcuts import render

# Create your views here.

def prueba_template(request):

    return render(request, "index.html")

def probando_padre(request):

    return render(request, "padre.html")

def iniciar(request):

    return render(request, "iniciar.html")

def crear_astronauta(request):

    return render(request, "crear_astronauta.html")
