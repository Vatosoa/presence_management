# Generated by Django 4.1.5 on 2023-06-22 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useregistration', '0045_presence_etudiant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='groupe',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='useregistration.groupe'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='section',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='useregistration.section'),
        ),
    ]