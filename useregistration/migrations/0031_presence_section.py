# Generated by Django 4.1.5 on 2023-06-20 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useregistration', '0030_presence'),
    ]

    operations = [
        migrations.AddField(
            model_name='presence',
            name='section',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='useregistration.section'),
        ),
    ]
