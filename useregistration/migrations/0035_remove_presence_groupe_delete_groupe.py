# Generated by Django 4.1.5 on 2023-06-21 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useregistration', '0034_presence_groupe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presence',
            name='groupe',
        ),
        migrations.DeleteModel(
            name='Groupe',
        ),
    ]
