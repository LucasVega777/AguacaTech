"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from becas import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), #Creamos la ruta raiz '' y la enlazamos con nuestra vista index del archivo views.py
    path('grado/', views.grado, name = 'grado'),
    path('doctorado/', views.doctorado, name = 'doctorado'),
    path('maestria/', views.maestrias, name = 'maestria'),
    path('noticias/', views.noticias, name = 'noticias'),
    path('idiomas/', views.idiomas, name = 'idiomas'),
    path('contacto/', views.contacto, name = 'contacto'),
    path('faq/', views.faq, name = 'faq'),
    path("sobre_nosotros/", views.sobre, name = "sobre_nosotros"),
    ]
