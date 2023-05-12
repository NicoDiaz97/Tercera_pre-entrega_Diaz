from django.db import models


class Barbero(models.Model):
    nombre          = models.CharField(max_length=64)
    apellido        = models.CharField(max_length=64)
    dni             = models.CharField(max_length=32)
    especialidad    = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Cliente(models.Model):
    nombre          = models.CharField(max_length=64)
    apellido        = models.CharField(max_length=64)
    dni             = models.CharField(max_length=32)
    telefono        = models.CharField(max_length=64)
    email           = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Servicio(models.Model):
    tipo                = models.CharField(max_length=64)
    duracion_minutos    = models.IntegerField()
    costo               = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.tipo} - Duración: {self.duracion_minutos}min - Costo: ${self.costo}.'

class Turno(models.Model):
    cliente     = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    barbero     = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    servicio    = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_turno = models.DateField()
    hora_turno  = models.TimeField()