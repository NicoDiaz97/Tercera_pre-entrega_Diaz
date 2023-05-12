from django import forms

class BarberoFormulario(forms.Form):
    nombre          = forms.CharField(required=True, max_length=64)
    apellido        = forms.CharField(required=True, max_length=64)
    dni             = forms.CharField(required=True, max_length=32)
    especialidad    = forms.CharField(required=True, max_length=256)