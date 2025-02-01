
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('notes/<int:note_id>', views.note_detail, name='note_detail'),
    path('success', views.addnote_success, name='addnote_success'),

]