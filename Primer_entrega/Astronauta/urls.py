from django.urls import path
from Astronauta import views


urlpatterns = [
    path("inicio/", views.prueba_template, name = "pagina_inicio"),
    path("padre/", views.probando_padre),
    path("iniciar/", views.iniciar, name = "pagina_iniciar"),
    path("crear_astronauta/", views.crear_astronauta, name = "crear_astronauta"),
    path("luna/", views.luna, name = "formulario_luna"),
    path("marte/", views.marte, name = "formulario_marte"),
    path("velocidad", views.velocidad_luz, name = "velocidad_luz"),
    path("buscar", views.buscar, name = "buscar" )
]