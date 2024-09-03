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
    Duración = models.PositiveIntegerField(help_text="Duración en minutos",null=True, blank=True)
    imagen = models.ImageField(upload_to='disco_img/', null=True, blank=True)
    Genero = models.ForeignKey(Genero, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.Titulo} - {self.Artista}"


