from django import forms
from .models import Source


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['name', 'source_type', 'organization', 'contact_info', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'source_type': forms.Select(attrs={'class': 'form-control'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }