from django import forms

from index.models import Usuario

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model= Usuario
        fields=['nombre_completo']
