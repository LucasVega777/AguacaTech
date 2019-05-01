from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Becas

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import Formulario



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


def programas (request):

    lista_grados = Becas.objects.filter(tipo_beca__nombre="programas")

    nombre_becas = { "name": lista_grados }

    return render(request, "programas.html", nombre_becas)



def contacto(request):
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            return HttpResponseRedirect ('/gracias/')
    else:
        form = Formulario()
    return render(request, "contacto.html", {'form': form})

from .secrets import contra
import smtplib


def gracias(request):
    message = " Hola, te escribimos del Soporte Tecnico, en estos momentos estaremos resolviendo su consulta, le rogamos paciencia, una respuesta con la  solucion deberia tardar entre unas 3 a 4 horas"
    subject = "Ayuda Consulta"
    message = "Subject: {}\n\n{} ".format(subject , message)

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login("contactosBecasPy.com", contra)

    server.sendmail("contactoBecasPy.com", "cesararroyolezcano@gmail.com",message)

    server.quit()

    return render (request, "gracias.html")
 


def sobre(request):
    return render(request, "sobre.html")


