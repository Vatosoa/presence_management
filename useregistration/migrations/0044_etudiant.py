# Generated by Django 4.1.5 on 2023-06-22 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useregistration', '0043_remove_presence_etudiant_delete_etudiant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('nom_etudiant', models.CharField(max_length=45)),
                ('prenom_etudiant', models.CharField(max_length=50)),
                ('image_etudiant', models.ImageField(default='k.jpeg', upload_to='image')),
                ('location_etudiant', models.CharField(blank=True, max_length=100)),
                ('groupe', models.ForeignKey(blank=True, default='Groupe 1', on_delete=django.db.models.deletion.CASCADE, to='useregistration.groupe')),
                ('section', models.ForeignKey(blank=True, default='Section 1', on_delete=django.db.models.deletion.CASCADE, to='useregistration.section')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
