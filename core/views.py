from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Note, NoteCategory
from .forms import NoteAddForm
def main(request):
    notes = Note.objects.all()
    category = request.GET.get('category')
    active_category = None
    if category:
        notes = notes .filter(category__id=category)
        active_category = NoteCategory.objects.get(id=category)
    categories = NoteCategory.objects.annotate(total_notes=Count('note'))
    note_form = NoteAddForm()
    if request.method == 'POST':
        note_form = NoteAddForm(request.POST)
        if note_form.is_valid():
            data = note_form.cleaned_data
            Note.objects.create(mark=data['mark'], category=data['category'])
            return redirect('addnote_success')
    return render(request, 'main.html', {'notes': notes, 'categories': categories, 'note_form': note_form, 'active_category': active_category,})

def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'note_detail.html', {'note': note})

def addnote_success(request):
    return render(request, 'addnote_success.html', )
