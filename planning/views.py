
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    created_at_display = forms.CharField(
        label='Създадена на',
        required=False,
        disabled=True,
        help_text='Това поле е само за преглед.'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.created_at:
            self.fields['created_at_display'].initial = (
                self.instance.created_at.strftime('%d.%m.%Y %H:%M')
            )
        else:
            self.fields['created_at_display'].initial = 'Ще се попълни автоматично'

    class Meta:
        model = Task
        fields = [
            'story', 'title', 'description', 'due_date', 'is_completed'
        ]
        error_messages = {
            'story': {
                'required': 'Моля, изберете материал за задачата.',
                'invalid_choice': 'Избраният материал не е валиден.',
            },
            'title': {
                'required': 'Моля, въведете заглавие на задачата.',
                'max_length': 'Заглавието на задачата е твърде дълго.',
            },
        }
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
                'class': 'form-control', 'rows': 3
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-control', 'type': 'datetime-local'
            }),
        }


def task_list(request):
    tasks = Task.objects.select_related('story').order_by(
        'is_completed', 'due_date'
    )
    return render(request, 'planning/task_list.html', {'tasks': tasks})


def task_create(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'planning/task_form.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'planning/task_form.html', {
        'form': form, 'task': task
    })


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'planning/task_confirm_delete.html', {
        'object': task, 'cancel_url': 'task_list'
    })
