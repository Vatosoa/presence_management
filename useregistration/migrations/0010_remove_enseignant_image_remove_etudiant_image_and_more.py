# Generated by Django 4.1.5 on 2023-06-12 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useregistration', '0009_etudiant_enseignant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseignant',
            name='image',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='image',
        ),
        migrations.AddField(
            model_name='enseignant',
            name='image_enseignant',
            field=models.ImageField(default='k.jpeg', upload_to='image'),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='image_admin',
            field=models.ImageField(default='k.jpeg', upload_to='image'),
        ),
    ]
