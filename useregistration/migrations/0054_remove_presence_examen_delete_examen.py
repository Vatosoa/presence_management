# Generated by Django 4.1.5 on 2023-06-22 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useregistration', '0053_alter_examen_enseignant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presence',
            name='examen',
        ),
        migrations.DeleteModel(
            name='Examen',
        ),
    ]
