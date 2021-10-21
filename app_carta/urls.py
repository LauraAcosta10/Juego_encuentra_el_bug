from django.urls import path
from .views import inicio,CrearPartida

urlpatterns = [
    path('',inicio,name="index"),
    path('Crear_partida/', CrearPartida, name="crear_partida"),
]