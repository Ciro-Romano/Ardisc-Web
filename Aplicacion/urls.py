from django.urls import path
from django.contrib import admin
from Aplicacion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('Discos/', views.Discos, name='Discos'),
    path('About/', views.About, name='About'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)