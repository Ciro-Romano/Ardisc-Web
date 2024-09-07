from django.urls import path
from django.contrib import admin
from Aplicacion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('Discos/', views.Discos, name='Discos'),
    path('About/', views.About, name='About'),
    path('Contacto/', views.Contacto, name='Contacto'),
    path('Consulta-envida/', views.Consulta_enviada, name="Consulta-Enviada"),
    path('Agregar-Disco/', views.AgregarDisco, name="Agregar-Disco"),
    path('Disco-Agregado/', views.Disco_agregado, name='Disco-Agregado'),
    path('Lista-Disco/', views.Lista_disco, name='Lista-Disco'),
    path('Editar-Disco/<id>/', views.Editar_Disco, name="Editar-Disco"),
    path('Disco-Editado/', views.Disco_Editado, name='Disco-Editado'),
    path('Eliminar-Disco/<id>/', views.Eliminar_Disco, name='Eliminar-Disco'),
    path('Disco-Eliminado/', views.Disco_eliminado, name='Disco-Eliminado'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    