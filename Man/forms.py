from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'address', 'city', 'state', 'zip']


    widget = {

        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'address': forms.TextInput(attrs={'class': 'form-control'}),
        'city': forms.TextInput(attrs={'class': 'form-control'}),
        'address': forms.TextInput(attrs={'class': 'form-control'}),
        'state': forms.TextInput(attrs={'class': 'form-control'}),
        'zip': forms.TextInput(attrs={'class': 'form-control'}),

    }    