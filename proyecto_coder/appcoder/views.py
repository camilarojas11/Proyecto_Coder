from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import *
from appcoder.forms import *

# Create your views here.

logo = "Mi Agenda Coder"
items = ["Home", "Usuarios", "Servicios", "Pagos", "Buscar"]

def index(request):
    id = 1
    h1_index = "Hola! Bienveni@ a la APP Coder"
    subtitulo_index = "La función de esta aplicación es poder ayudarte a mantener actualizado el pago de tus facturas."
    dict_context = {'id': id, 'h1_index': h1_index, 'items': items, 'subtitulo_index':subtitulo_index, 'logo': logo}
    return render(request, 'appcoder/index.html',dict_context)



def usuarios(request):
    id = 2
    h1_usuarios = "Usuarios"
    subtitulo_user = "En esta página podra ingresar y guardar su usuario."
    
    usuarios = Usuario.objects.all()
    
    if request.method == "POST":
        miUsuario = UserFormulario(request.POST)
        
        if miUsuario.is_valid():
            informacion = miUsuario.cleaned_data
            usuario = Usuario(nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'])
            usuario.save()
            
            miUsuario = UserFormulario()
            return render(request, 'appcoder/usuarios.html',{'id': id,'h1_usuarios': h1_usuarios, 'subtitulo_user': subtitulo_user, 'logo': logo, 'items': items, 'usuarios': usuarios ,'miUsuario': miUsuario})

    else:
        miUsuario = UserFormulario()
        return render(request, 'appcoder/usuarios.html',{'id': id,'h1_usuarios': h1_usuarios, 'subtitulo_user': subtitulo_user, 'logo': logo, 'items': items,'usuarios': usuarios ,'miUsuario': miUsuario})



def servicios(request):
    id = 3
    h1_servicios = "Cargar Servicios"
    subtitulo_service = "Aqui podra ingresar los datos de las facturas/servicios pendientes por abonar."    
    servicios = Servicio.objects.all()
    
    if request.method == "POST":
        miServicio = ServiceFormulario(request.POST)
        
        if miServicio.is_valid():
            informacion = miServicio.cleaned_data
            servicio = Servicio(numero_cliente=informacion['numero_cliente'], nombre_empresa=informacion['nombre_empresa'], importe_factura=informacion['importe_factura'])
            servicio.save()
            
            miServicio = ServiceFormulario()
            return render(request, 'appcoder/servicios.html',{'id': id,'h1_servicios': h1_servicios, 'subtitulo_service': subtitulo_service, 'logo': logo, 'items': items, 'servicios': servicios ,'miServicio': miServicio})

    else:
        miServicio = ServiceFormulario()
        return render(request, 'appcoder/servicios.html',{'id': id,'h1_servicios': h1_servicios, 'subtitulo_service': subtitulo_service, 'logo': logo, 'items': items, 'servicios': servicios ,'miServicio': miServicio})



def pagos(request):
    id = 4
    h1_pagos = "Cargar Pagos Efectuados"
    subtitulo_pagos = "En esta página podra cargar la información de los pagos efectuados de facturas/servicios."  
    pagos = PagoDeServicios.objects.all()
    
    if request.method == "POST":
        miPago = PagoFormulario(request.POST)
        
        if miPago.is_valid():
            informacion = miPago.cleaned_data
            pago = PagoDeServicios(numero_comprobante=informacion['numero_comprobante'], monto_pagado=informacion['monto_pagado'], check_pago=informacion['check_pago'])
            pago.save()
            
            miPago = PagoFormulario()
            return render(request, 'appcoder/pagos.html',{'id': id,'h1_pagos': h1_pagos, 'subtitulo_pagos': subtitulo_pagos, 'logo': logo, 'items': items, 'pagos': pagos ,'miPago': miPago})

    else:
        miPago = PagoFormulario()
        return render(request, 'appcoder/pagos.html',{'id': id,'h1_pagos': h1_pagos, 'subtitulo_pagos': subtitulo_pagos, 'logo': logo, 'items': items, 'pagos': pagos ,'miPago': miPago})



def buscar(request):
    id = 5
    h1_buscar = "Página de Busquedas"
    subtitulo_search = "Haga clic en el acceso directo según lo que desee buscar."
    dict_context = {'id': id, 'h1_buscar': h1_buscar, 'items': items, 'subtitulo_search':subtitulo_search, 'logo': logo}
    return render(request, 'appcoder/buscar.html',dict_context)



def buscarUsuario(request):
    id = 6
    h1_buscar = "Buscar Usuario"
    subtitulo_search = "Ingrese la información solicitada para generar la búsqueda de usuario"
    
    data = request.GET.get('dni', "")
    error = ""

    if data:
        try:
            usuario = Usuario.objects.get(dni = data)
            return render(request, 'appcoder/buscarUsuario.html', {"id":id, 'h1_buscar': h1_buscar, 'subtitulo_search': subtitulo_search , 'items':items ,'logo': logo, "usuario": usuario, "id": data})

        except Exception as exc:
            print(exc)
            error = "No existe el usuario ingresado. Por favor intente nuevamente."
    return render(request, 'appcoder/buscarUsuario.html',{"id":id, 'h1_buscar': h1_buscar, 'subtitulo_search': subtitulo_search , 'items': items, 'logo': logo, "error": error})
