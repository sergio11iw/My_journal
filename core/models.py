from django.db import models

class Note(models.Model):
    mark = models.CharField(max_length=100, verbose_name='Отметить')



    class Meta:
        verbose_name = 'Наблюдение'
        verbose_name_plural = 'Наблюдения'
    def __str__(self):
        return self.mark
