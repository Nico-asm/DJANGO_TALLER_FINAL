from django.db import models

# Create your models here.

##### Se debe ingresar por BD #####
class Institucion(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

opcion_estado = [
    ['R','Reservado'],
    ['C','Completada'],
    ['A','Anulada'],
    ['N','No Asisten']
]


class Inscritos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    fechaInscripcion = models.DateField(verbose_name='Fecha Inscripción')
    horaInscripcion = models.TimeField(verbose_name='Hora Inscripción')
    estado = models.CharField(max_length=1,choices=opcion_estado)
    observacion = models.TextField(max_length=300, null=True, blank=True, verbose_name='Observación')

    def __str__(self):
        return self.nombre