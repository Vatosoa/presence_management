# Generated by Django 4.1.5 on 2023-06-17 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useregistration', '0018_rename_exam_presence_examen'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='petit_nom_module',
            field=models.CharField(default='..', max_length=10),
        ),
        migrations.AlterField(
            model_name='module',
            name='enseignant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='useregistration.enseignant'),
        ),
        migrations.AlterField(
            model_name='module',
            name='nom_module',
            field=models.CharField(max_length=100),
        ),
    ]
