# Generated by Django 5.1.4 on 2024-12-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_note_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(auto_now_add=True, default=1, verbose_name='Дата'),
            preserve_default=False,
        ),
    ]