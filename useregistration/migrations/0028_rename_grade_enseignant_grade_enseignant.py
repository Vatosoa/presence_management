# Generated by Django 4.1.5 on 2023-06-17 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useregistration', '0027_groupe_etudiant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enseignant',
            old_name='grade',
            new_name='grade_enseignant',
        ),
    ]