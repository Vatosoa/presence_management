# Generated by Django 4.1.5 on 2023-06-17 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useregistration', '0024_alter_groupe_etudiant_alter_groupe_salle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examen',
            name='nom_examen',
        ),
        migrations.RemoveField(
            model_name='groupe',
            name='etudiant',
        ),
        migrations.RemoveField(
            model_name='groupe',
            name='section',
        ),
        migrations.AddField(
            model_name='examen',
            name='module',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='useregistration.module'),
        ),
        migrations.AlterField(
            model_name='salle',
            name='id_salle',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
