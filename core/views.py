from django.shortcuts import render, redirect,  get_object_or_404
from django.db.models import Count
from .models import Note, NoteCategory
from .forms import NoteAddForm, NoteAddModelForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

@login_required
def main(request):
    profile = request.user.profile
    notes = Note.objects.filter(profile=profile)
    category = request.GET.get('category')
    active_category = None
    notes_count = notes.count()
    if category:
        notes = notes .filter(category__id=category)
        active_category = NoteCategory.objects.get(id=category)

    categories = NoteCategory.objects.annotate(total_notes=Count('note'))

    form = NoteAddModelForm()
    if request.method == 'POST':
        form = NoteAddModelForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.profile = profile
            note.save()
            return redirect('addnote_success')

    return render(request, 'main.html', {'notes': notes, 'categories': categories, 'form': form, 'active_category': active_category, 'notes_count': notes_count,})

def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'note_detail.html', {'note': note})

def addnote_success(request):
    return render(request, 'addnote_success.html')

@login_required
def note_edit(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if not Note.objects.filter(profile=request.user.profile, id=note_id).exists():
        raise Http404
    note_form = NoteAddModelForm(instance=note)
    if request.method == 'POST':
        note_form = NoteAddModelForm(request.POST, request.FILES, instance=note)
        if note_form.is_valid():
            note_form.save()
            return redirect('note_detail', note_id)
    return render(request, 'note_edit.html', {'note_form': note_form})

@login_required
def note_delete(request, note_id):
    if not Note.objects.filter(profile=request.user.profile, id=note_id).exists():
        raise Http404
    post = Note.objects.get(id=note_id)
    post.delete()
    return redirect('main')
