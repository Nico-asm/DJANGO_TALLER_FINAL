# Generated by Django 4.1 on 2022-12-20 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario_app', '0012_alter_inscritos_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscritos',
            name='telefono',
            field=models.CharField(max_length=8),
        ),
    ]
