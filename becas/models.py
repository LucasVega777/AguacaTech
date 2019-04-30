from django.db import models

from django import forms

# Create your models here.
tipo_de_beca = (
        ('g', 'grado'),
        ('p', 'postgrado'),
        ('d', 'doctorado'),
        )

class Becas(models.Model): #solo clases en mayuscula
    tipo = models.CharField(max_length=1, choices=tipo_de_beca)
    nombre_programa = models.CharField(max_length=100) #Campo/columna titulo de tipo "campo de caracteres" de longitud maxima de 100
    descripcion = models.TextField(null=True, blank=True) #Campo/columna titulo de tipo Texto, los argumentos blank y null son para que el campo sea opcional
    requisito = models.TextField(null=True, blank=True)
    duracion = models.CharField(max_length=50)
    contactos = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre_programa