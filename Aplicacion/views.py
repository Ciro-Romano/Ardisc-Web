from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from .models import Genero, Disco
from . forms import ContactoFormulario, DiscoFormulario

# Create your views here.
def Inicio(request):
    return render(request, 'aplicacion/inicio.html')

def Discos(request):
    discos = Disco.objects.all()  
    return render(request, 'aplicacion/discos.html', {'discos': discos})
   

def About(request):
    return render(request, 'aplicacion/about.html')

def Contacto(request):
    if request.method == 'POST':
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Consulta-Enviada')
    else:
        formulario = ContactoFormulario()

    return render(request, 'aplicacion/contacto.html', {'formulario': formulario})

def Consulta_enviada(request):
    return render(request, 'aplicacion/Exito/consulta-enviada.html')

def AgregarDisco(request):
    if request.method == 'POST':
        formulario = DiscoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Disco-Agregado')
    else:
        formulario = DiscoFormulario()

    return render(request, 'aplicacion/crud/agregar-disco.html', {'formulario': formulario})

def Disco_agregado(request):
    return render(request, 'aplicacion/Exito/disco-agregado.html')

def Lista_disco(request):
    disco = Disco.objects.all()
    return render(request, 'aplicacion/crud/lista.html', {'disco': disco})


