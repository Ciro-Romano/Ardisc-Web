from typing import Any
from django.db import models

# Create your models here.
class Genero(models.Model):
    Nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.Nombre

class Disco(models.Model):
    Titulo = models.CharField(max_length=40)
    Artista = models.CharField(max_length=40)
    Descripcion = models.TextField()
    Publicacion =  models.DateField() 
    Estudio = models.CharField(max_length=40,null=True, blank=True)
    Discografica = models.CharField(max_length=40,null=True, blank=True)
    Imagen = models.ImageField(upload_to='disco_img/', null=True, blank=True)
    Genero = models.ForeignKey(Genero, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.Titulo} - {self.Artista}"

Tipo_de_consulta = [
    [0, 'Consulta'],
    [1, 'Sugerencia'],
    [2, 'Otro'],
]

class Contacto(models.Model):
    Nombre = models.CharField(max_length=30)
    Email = models.EmailField()
    Tipo = models.IntegerField(choices=Tipo_de_consulta)
    Mensaje = models.TextField()
    Fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Nombre} - {self.Tipo} - {self.Fecha}"
    
