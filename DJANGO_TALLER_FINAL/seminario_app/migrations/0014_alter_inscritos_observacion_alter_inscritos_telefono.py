# Generated by Django 4.1 on 2022-12-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario_app', '0013_alter_inscritos_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscritos',
            name='observacion',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Observación'),
        ),
        migrations.AlterField(
            model_name='inscritos',
            name='telefono',
            field=models.CharField(max_length=8, verbose_name='Teléfono'),
        ),
    ]
