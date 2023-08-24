from django import forms
from .models import *

# class ArizaForm(forms.ModelForm):
#     class Meta:
#         model = Ariza
#         fields = '__all__'
#         widgets = {
#             'ism': forms.TextInput(attrs={'class': 'form-control'}),
#             'familiya': forms.TextInput(attrs={'class': 'form-control'}),
#             'sharifi': forms.TextInput(attrs={'class': 'form-control'}),
#             'mamlakat': forms.Select(attrs={'class': 'form-control'}),
#             'viloyat': forms.Select(attrs={'class': 'form-control'}),
#             'tuman': forms.TextInput(attrs={'class': 'form-control'}),
#             'jinsi': forms.Select(attrs={'class': 'form-control'}),
#             'pasport': forms.TextInput(attrs={'class': 'form-control'}),
#             'pasport_num': forms.NumberInput(attrs={'class': 'form-control'}),
#             'manzil': forms.TextInput(attrs={'class': 'form-control'}),
#             'fakultet': forms.Select(attrs={'class': 'form-control'}),
#             'yunalish': forms.TextInput(attrs={'class': 'form-control'}),
#             'grux': forms.TextInput(attrs={'class': 'form-control'}),
#             'kurs': forms.Select(attrs={'class': 'form-control'}),
#             'telefon': forms.NumberInput(attrs={'class': 'form-control'}),
#             'uploaded_file': forms.FileInput(attrs={'class': 'form-control-file'}),
#         }


class ArizaForm(forms.ModelForm):
    class Meta:
        model = Ariza
        fields = '__all__'