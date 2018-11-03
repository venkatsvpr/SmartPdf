from django import forms
from django.forms import formset_factory


class FileForm(forms.Form):
    name = forms.CharField(
        label='File Name:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter File Name here'
        })
    )
    
    pages = forms.CharField(
        label='Enter page range:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '1-5,7'
        })
    )
    
FileFormset = formset_factory(FileForm, extra=1)
