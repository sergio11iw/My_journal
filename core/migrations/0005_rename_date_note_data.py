# Generated by Django 5.1.4 on 2024-12-29 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_note_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='date',
            new_name='data',
        ),
    ]
