# Generated by Django 4.2 on 2023-05-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('ALPINE', 'Alpine'), ('ASTON MARTIN', 'Aston Martin'), ('FERRARI', 'Ferrari'), ('RED BULL', 'Red Bull'), ('MERCEDES', 'Mercedes'), ('MCLAREN', 'Mclaren')], default='', max_length=100),
        ),
    ]
