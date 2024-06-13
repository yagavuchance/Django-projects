from django import forms
from .import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Manunited
        fields = ['Name','Number',"Age",'country','image']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'Number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number'}),
            'Age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }