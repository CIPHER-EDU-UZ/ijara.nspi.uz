from django import forms
from .models import *

class ArizaForm(forms.ModelForm):
    class Meta:
        model = Ariza
        fields = '__all__'
