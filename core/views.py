from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Note, NoteCategory
from .forms import NoteAddForm, NoteAddModelForm
def main(request):
    notes = Note.objects.all()
    category = request.GET.get('category')
    active_category = None
    if category:
        notes = notes .filter(category__id=category)
        active_category = NoteCategory.objects.get(id=category)
    categories = NoteCategory.objects.annotate(total_notes=Count('note'))

    form = NoteAddModelForm()
    if request.method == 'POST':
        form = NoteAddModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addnote_success')

    return render(request, 'main.html', {'notes': notes, 'categories': categories, 'form': form, 'active_category': active_category,})

def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'note_detail.html', {'note': note})

def addnote_success(request):
    return render(request, 'addnote_success.html', )
