from django import forms
from .models import Source


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ["name", "source_type", "organization", "contact_info", "notes"]
        labels = {
            "name": "Име на източника",
            "source_type": "Тип източник",
            "organization": "Организация",
            "contact_info": "Контактна информация",
            "notes": "Бележки",
        }
        help_texts = {
            "name": "Въведете име, по което лесно ще разпознаете източника.",
            "source_type": "Изберете най-подходящия тип.",
            "organization": "Организация или институция, ако е приложимо.",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Име на източника..."
            }),
            "source_type": forms.Select(attrs={"class": "form-control"}),
            "organization": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Организация..."
            }),
            "contact_info": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имейл, сайт или контакт..."
            }),
            "notes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Допълнителни бележки..."
            }),
        }
