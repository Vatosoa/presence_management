# Generated by Django 4.1.5 on 2023-06-15 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useregistration', '0014_remove_administrateur_id_remove_enseignant_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salle',
            name='id_salle',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
