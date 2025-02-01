from django import forms
from .models import NoteCategory, Note



class NoteAddForm(forms.Form):
    mark = forms.CharField(label='Текст', widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=NoteCategory.objects.all(), label='Категория')

