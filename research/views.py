
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .forms import SourceForm
from .models import Source, Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["story", "title", "content"]
        labels = {
            "story": "Материал",
            "title": "Заглавие на бележката",
            "content": "Съдържание",
        }
        help_texts = {
            "story": "Изберете материала, към който принадлежи бележката.",
            "content": "Запишете важните факти, идеи или цитати.",
        }
        widgets = {
            "story": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Заглавие на бележката..."
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Напишете бележката..."
            }),
        }


def source_list(request):
    sources = Source.objects.all().order_by('name')
    return render(request, 'research/source_list.html', {'sources': sources})


def source_create(request):
    form = SourceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('source_list')
    return render(request, 'research/source_form.html', {'form': form})


def source_edit(request, pk):
    source = get_object_or_404(Source, pk=pk)
    form = SourceForm(request.POST or None, instance=source)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('source_list')
    return render(request, 'research/source_form.html', {
        'form': form, 'source': source
    })


def source_delete(request, pk):
    source = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        source.delete()
        return redirect('source_list')
    return render(request, 'research/source_confirm_delete.html', {
        'object': source, 'cancel_url': 'source_list'
    })


def note_list(request):
    notes = Note.objects.select_related('story').order_by('-created_at')
    return render(request, 'research/note_list.html', {'notes': notes})


def note_create(request):
    form = NoteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'research/note_form.html', {'form': form})


def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'research/note_form.html', {
        'form': form, 'note': note
    })


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'research/note_confirm_delete.html', {
        'object': note, 'cancel_url': 'note_list'
    })
