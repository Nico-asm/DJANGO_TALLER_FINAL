# Generated by Django 4.1 on 2022-12-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario_app', '0002_inscritos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscritos',
            name='horaInscripcion',
            field=models.TimeField(),
        ),
    ]
