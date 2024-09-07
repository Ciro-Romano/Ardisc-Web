from django.shortcuts import render,redirect, get_list_or_404 , get_object_or_404
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

def Editar_Disco(request, id):
    disco = Disco.objects.get(id=id)
    formulario = DiscoFormulario(instance=disco)
    if request.method == 'POST':
        formulario = DiscoFormulario(data=request.POST, instance=disco, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('Disco-Editado')
    {'formulario' : formulario}
    return render(request, 'aplicacion/crud/editar.html', {'formulario': formulario})

def Disco_Editado(request):
    return render(request, 'aplicacion/Exito/disco-editado.html')

def Eliminar_Disco(request, id):
    disco = get_object_or_404(Disco, id=id)

    if request.method == 'POST':
        disco.delete()
        return redirect('Disco-Eliminado')
    return render(request, 'aplicacion/Confirmar/confirmar.html', {'disco': disco})

def Disco_eliminado(request):
    return render(request, 'aplicacion/Exito/disco-eliminado.html')
