from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request, 'aplicacion/inicio.html')

def Discos(request):
    return render(request, 'aplicacion/discos.html')

def About(request):
    return render(request, 'aplicacion/about.html')
