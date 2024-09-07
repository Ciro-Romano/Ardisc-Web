from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout

def login_request(request):
    
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "aplicacion/inicio.html")

        msg_login = "Usuario o contraseña incorrectos"

    print(f"Usuario autenticado en la vista: {request.user.is_authenticated}")

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('Inicio')  
        else:
            messages.error(request, 'Error en los datos ingresados. Por favor, corrige los errores.')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

def Logout(request):
    logout(request)  
    return redirect('Inicio')