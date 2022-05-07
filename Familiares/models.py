from django.db import models

# Create your models here.
class Familiar (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()
    edad = models.IntegerField()

    def __srt__(self):
        return f'{self.nombre} {self.apellido}'