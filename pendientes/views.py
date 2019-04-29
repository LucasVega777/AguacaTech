from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Tarea
# Create your views here.

def index(request):
    return render(request, "index.html")

def postgrado(request):
    return render(request, "postgrado.html")


def grado(request):
    return render(request, "grado.html")


def doctorado(request):
    return render(request, "doctorado.html")


def noticias(request):
    return render(request, "noticias.html")