# Generated by Django 4.1.5 on 2023-06-17 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useregistration', '0016_remove_examen_id_salle_remove_groupe_id_etudiant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presence',
            name='etudiant',
        ),
        migrations.AddField(
            model_name='presence',
            name='etudiant',
            field=models.ManyToManyField(to='useregistration.etudiant'),
        ),
    ]
