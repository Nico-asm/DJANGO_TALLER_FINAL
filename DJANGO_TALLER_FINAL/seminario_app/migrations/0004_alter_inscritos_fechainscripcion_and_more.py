# Generated by Django 4.1 on 2022-12-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario_app', '0003_alter_inscritos_horainscripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscritos',
            name='fechaInscripcion',
            field=models.DateField(verbose_name='Fecha Inscripción'),
        ),
        migrations.AlterField(
            model_name='inscritos',
            name='horaInscripcion',
            field=models.TimeField(verbose_name='Hora Inscripción'),
        ),
    ]
