# Generated by Django 3.1.2 on 2020-11-19 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appLibreria', '0002_auto_20201119_0939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comic',
            old_name='coleccion_id',
            new_name='coleccion',
        ),
    ]
