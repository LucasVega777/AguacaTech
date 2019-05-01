from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    número = forms.CharField()
    mensaje = forms.CharField(max_length=100)

   
