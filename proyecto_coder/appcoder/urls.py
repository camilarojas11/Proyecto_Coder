from operator import index
from unicodedata import name
from django.urls import path
from appcoder.views import *


urlpatterns = [
    path('', index, name= "home"),
    path('usuarios/', usuarios, name= "users"),
    path('servicios/', servicios, name= "cargar_servicio"),
    path('pagos/', pagos, name= "agendar_pagos"),
    path('buscar/', buscar, name= 'buscar'),
]
