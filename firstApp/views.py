from re import S
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
#Crear primera vista en python


def display(request):
    return HttpResponse("<h1>Hola Mundo Jorge!!</h1>")



#segunda vista de nuestra app

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha Y Hora Actual: </b>"+str(dt)
    return HttpResponse(s)


#crear boton

def boton(request):
    return HttpResponse("<BUTTON>Enviar</BUTTON>")