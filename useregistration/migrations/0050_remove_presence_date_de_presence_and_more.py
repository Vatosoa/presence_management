# Generated by Django 4.1.5 on 2023-06-22 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useregistration', '0049_alter_enseignant_module'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presence',
            name='date_de_presence',
        ),
        migrations.RemoveField(
            model_name='presence',
            name='section',
        ),
        migrations.AddField(
            model_name='examen',
            name='date_examen',
            field=models.DateField(default='2023-01-01'),
        ),
        migrations.AddField(
            model_name='presence',
            name='enseignant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='useregistration.enseignant'),
        ),
    ]
