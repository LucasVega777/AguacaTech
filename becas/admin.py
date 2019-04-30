from django.contrib import admin

from .models import Becas 

from .models import TipoBeca

#importamos el modelo

# Register your models here.

admin.site.register(Becas) # lo registramos

admin.site.register(TipoBeca)