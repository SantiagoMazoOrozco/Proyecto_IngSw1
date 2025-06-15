from django import forms
from .models import Perfil

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar']
