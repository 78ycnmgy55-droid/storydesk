from django import forms
from .models import Story, Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'description']
        error_messages = {
            'name': {
                'required': 'Моля, въведете име на темата.',
                'max_length': 'Името на темата е твърде дълго.',
            },
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Име на темата...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Описание...'
            }),
        }
        labels = {
            'name': 'Име',
            'description': 'Описание',
        }


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = [
            'topic', 'title', 'summary',
            'status', 'deadline', 'sources'
        ]
        error_messages = {
            'topic': {
                'required': 'Моля, изберете тема.',
                'invalid_choice': 'Избраната тема не е валидна.',
            },
            'title': {
                'required': 'Моля, въведете заглавие на материала.',
                'max_length': 'Заглавието не може да е по-дълго от 200 символа.',
            },
            'status': {
                'required': 'Моля, изберете статус.',
                'invalid_choice': 'Моля, изберете валиден статус.',
            },
        }
        widgets = {
            'topic': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Въведете заглавие на материала...'
            }),
            'summary': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Кратко резюме или описание...'
            }),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'deadline': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'sources': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'topic': 'Тема',
            'title': 'Заглавие',
            'summary': 'Резюме',
            'status': 'Статус',
            'deadline': 'Краен срок',
            'sources': 'Източници',
        }
        help_texts = {
            'title': 'Изберете ясно и отличително заглавие.',
            'summary': 'Опишете накратко същността на материала.',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and not title.strip():
            raise forms.ValidationError(
                "Заглавието не може да съдържа само интервали."
            )
        return title