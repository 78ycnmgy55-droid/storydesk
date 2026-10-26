from django.shortcuts import render, redirect
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'story',
            'title',
            'description',
            'due_date',
            'is_completed',
        ]
        labels = {
            'story': 'Материал',
            'title': 'Заглавие',
            'description': 'Описание',
            'due_date': 'Краен срок',
            'is_completed': 'Изпълнена',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
        }


def task_list(request):
    tasks = Task.objects.select_related('story').order_by('is_completed', 'due_date')
    return render(request, 'planning/task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'planning/task_form.html', {'form': form})