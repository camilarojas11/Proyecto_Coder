from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from appcoder.models import Usuario, Servicio, PagoDeServicios


# Create your views here.
logo = "App Coder"
items = ["Home", "Usuarios", "Servicios", "Pagos"]

def index(request):
    id = 1
    h1_index = "Hola! Bienveni@ a la APP Coder"
    subtitulo_index = "Esta entrega corresponde a la primer entrega del proyecto final."
    dict_context = {'id': id, 'h1_index': h1_index, 'items': items, 'subtitulo_index':subtitulo_index, 'logo': logo}
    return render(request, 'appcoder/index.html',dict_context)

