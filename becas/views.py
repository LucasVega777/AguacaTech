from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Becas
# Create your views here.

def index(request):
    return render(request, "index.html")

def doctorado(request):

    lista_grados = Becas.objects.filter(tipo_beca__nombre="Doctorado")

    nombre_becas = { "name": lista_grados }

    return render(request, "doctorado.html", nombre_becas)


def grado(request):
    lista_grados = Becas.objects.filter(tipo_beca__nombre="Grado")

    nombre_becas = { "name": lista_grados }

    return render(request, "grado.html", nombre_becas)


def maestrias(request):

    lista_grados = Becas.objects.filter(tipo_beca__nombre="Maestria")

    nombre_becas = { "name": lista_grados }

    return render(request, "maestria.html", nombre_becas)



def noticias(request):
    
    return render(request, "noticias.html")



def faq(request):
    return render(request, "faq.html")



def idiomas(request):

    lista_grados = Becas.objects.filter(tipo_beca__nombre="idiomas")

    nombre_becas = { "name": lista_grados }

    return render(request, "idiomas.html", nombre_becas)



def contacto(request):
    return render(request, "contacto.html")


def sobre(request):
    return render(request, "sobre.html")
