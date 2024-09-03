from django.urls import path
from django.contrib import admin
from Aplicacion import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
]