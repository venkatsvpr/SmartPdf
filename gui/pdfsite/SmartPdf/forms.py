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
        required = False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '1-5,7'
        })
    )
    
    check = forms.BooleanField(
        label = 'Include all pages?',
        initial = False,
        required = False,
        widget=forms.CheckboxInput()
    )
    
FileFormset = formset_factory(FileForm, extra=1)
