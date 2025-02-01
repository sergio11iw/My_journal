
from django.db import models

class NoteCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self. title
class Note(models.Model):
    mark = models.CharField(max_length=100, verbose_name='Отметить')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey(NoteCategory, blank=True, null=True, on_delete=models.SET_NULL,
                                 verbose_name='Категория')


    class Meta:
        verbose_name = 'Наблюдение'
        verbose_name_plural = 'Наблюдения'

    def __str__(self):
        return self.mark
