# Generated by Django 3.1.2 on 2020-11-19 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appLibreria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comic',
            old_name='autor',
            new_name='coleccion_id',
        ),
    ]