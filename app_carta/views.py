from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Token
import secrets
import random

# Create your views here.


def inicio(request):
    return render(request,"index.html")

def CrearPartida(request):
    x = secrets.token_hex(6)
    token = x[0:5]
    codigo=Token.objects.create(token=token)
    return render(request,"dueñoPartida.html",{'token':codigo})
