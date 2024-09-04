from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from .models import Genero, Disco
from . forms import ContactoFormulario

# Create your views here.
def Inicio(request):
    return render(request, 'aplicacion/inicio.html')

def Discos(request):
    discos = Disco.objects.all()  
    return render(request, 'aplicacion/discos.html', {'discos': discos})
   

def About(request):
    return render(request, 'aplicacion/about.html')

def Contacto(request):
    consulta = {'formulario': ContactoFormulario()}
    if request.method == 'POST':
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Consulta-Enviada')
    else:
        formulario = ContactoFormulario()

    return render(request, 'aplicacion/contacto.html', consulta)

def Consulta_enviada(request):
    return render(request, 'aplicacion/consulta-enviada.html')
