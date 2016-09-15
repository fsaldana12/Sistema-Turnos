from django import forms
from .models import *

class pacienteForm(forms.ModelForm):
    class Meta:
        model=Paciente
        fields=('nombre','apellido','dni','telefono','fechaNacimiento','obraSocial','numeroObraSocial',)