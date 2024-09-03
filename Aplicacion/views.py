from django.shortcuts import render
from .models import Genero, Disco

# Create your views here.
def Inicio(request):
    return render(request, 'aplicacion/inicio.html')

def Discos(request):
    discos = Disco.objects.all()  
    return render(request, 'aplicacion/discos.html', {'discos': discos})
   

def About(request):
    return render(request, 'aplicacion/about.html')
