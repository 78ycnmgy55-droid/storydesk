from django.shortcuts import render, redirect, get_object_or_404
from .forms import SourceForm
from .models import Source, Note
from stories.models import Story
from django import forms


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['story', 'title', 'content']
        labels = {
            'story': 'Материал',
            'title': 'Заглавие',
            'content': 'Съдържание',
        }


def source_list(request):
    sources = Source.objects.all().order_by('name')
    return render(request, 'research/source_list.html', {'sources': sources})


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('source_list')
    else:
        form = SourceForm()

    return render(request, 'research/source_form.html', {'form': form})


def note_list(request):
    notes = Note.objects.select_related('story').order_by('-created_at')
    return render(request, 'research/note_list.html', {'notes': notes})


def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'research/note_form.html', {'form': form})