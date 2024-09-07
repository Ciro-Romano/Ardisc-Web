from django.shortcuts import render,redirect, get_list_or_404 , get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import Genero, Disco
from . forms import ContactoFormulario, DiscoFormulario
from django.contrib.auth.decorators import login_required
# Create your views here.
def Inicio(request):
    return render(request, 'aplicacion/inicio.html')

@login_required
def Discos(request):
    discos = Disco.objects.all()  
    return render(request, 'aplicacion/discos.html', {'discos': discos})
   
@login_required
def About(request):
    return render(request, 'aplicacion/about.html')

@login_required
def Contacto(request):
    if request.method == 'POST':
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Consulta-Enviada')
    else:
        formulario = ContactoFormulario()

    return render(request, 'aplicacion/contacto.html', {'formulario': formulario})

@login_required
def Consulta_enviada(request):
    return render(request, 'aplicacion/Exito/consulta-enviada.html')

@login_required
def AgregarDisco(request):
    if request.method == 'POST':
        formulario = DiscoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Disco-Agregado')
    else:
        formulario = DiscoFormulario()

    return render(request, 'aplicacion/crud/agregar-disco.html', {'formulario': formulario})

@login_required
def Disco_agregado(request):
    return render(request, 'aplicacion/Exito/disco-agregado.html')

@login_required
def Lista_disco(request):
    disco = Disco.objects.all()
    return render(request, 'aplicacion/crud/lista.html', {'disco': disco})

@login_required
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

@login_required
def Disco_Editado(request):
    return render(request, 'aplicacion/Exito/disco-editado.html')

@login_required
def Eliminar_Disco(request, id):
    disco = get_object_or_404(Disco, id=id)

    if request.method == 'POST':
        disco.delete()
        return redirect('Disco-Eliminado')
    return render(request, 'aplicacion/Confirmar/confirmar.html', {'disco': disco})

@login_required
def Disco_eliminado(request):
    return render(request, 'aplicacion/Exito/disco-eliminado.html')
