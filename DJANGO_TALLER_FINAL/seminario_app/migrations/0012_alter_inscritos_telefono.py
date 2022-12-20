# Generated by Django 4.1 on 2022-12-19 23:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario_app', '0011_alter_inscritos_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscritos',
            name='telefono',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Solo puede ingresar Numeros', regex='^\\d+$')]),
        ),
    ]
