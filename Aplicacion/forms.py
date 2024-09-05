from django import forms
from .models import Contacto , Disco

class ContactoFormulario(forms.ModelForm):
    class Meta: 
        model = Contacto
        fields = '__all__'

class DiscoFormulario(forms.ModelForm):
    class Meta:
        model = Disco
        fields = '__all__'
