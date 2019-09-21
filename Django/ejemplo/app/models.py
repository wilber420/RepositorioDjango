from django.db import models
from django.contrib.auth import get_user_model
from django import forms


# Create your models here.

User = get_user_model()


class Alumno(models.Model):

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=200)
    carne = models.CharField(max_length=20)
    SEXO = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=SEXO, default='M')

    def __str__(self):
        return "{0} ,{1} ".format(self.nombre,self.apellido)

class Carrera(models.Model):

    alumno = models.ForeignKey(Alumno,null=False, blank=False, on_delete=models.CASCADE)
    carrera = models.CharField(max_length=100)

    def __str__(self):
        return "{0}, {1}" .format(self.alumno, self.carrera)




class Nota(models.Model):

    alumno = models.ForeignKey(Alumno,null=False,blank=False, on_delete=models.CASCADE)
    programación =models.CharField(max_length=2)
    sistemas_Operativos=models.CharField(max_length=2)
    Fisica=models.CharField(max_length=2)
    POO=models.CharField(max_length=2)


    def __str__(self):
        return "{0}" .format(self.alumno)

