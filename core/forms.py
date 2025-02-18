from django import forms
from .models import NoteCategory, Note

class NoteAddForm(forms.Form):
    mark = forms.CharField(label='Текст', widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=NoteCategory.objects.all(), label='Категория')

class NoteAddModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['profile']