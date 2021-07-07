from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'doctor'),
      (2, 'paciente'),
      (3, 'sectretario')
  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, default=2)


class Paciente(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='el_paciente')
    nacimiento = models.DateField(blank=True)
    cedula = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=20)
    barrio = models.CharField(max_length=20)
    telefono = models.PositiveIntegerField()
    aseguradora = models.CharField(max_length=20)
    ocupacion = models.CharField(max_length=20)
    grupo_sanguineo = models.CharField(max_length=20)
    num_hijos = models.PositiveSmallIntegerField()
    correo = models.EmailField()
    estado_civil = models.CharField(max_length=10)
    #Alergias_a_medicamentos = models.CharField(max_length=100)
    #Enfermedades_que_padece = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

#sclass cita(models.Model):
#s    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='el_paciente')
#s    Razon_de_la_Consulta = models.CharField(max_length=100)
#s    fecha = models.DateTimeField()



class Doctor(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='el_doctor')
    nacimiento = models.DateField(blank=True)
    cedula = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=20)
    barrio = models.CharField(max_length=20)
    telefono = models.PositiveIntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.correo

class Secretario(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='el_secretario')
    nacimiento = models.DateField(blank=True)
    cedula = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=20)
    barrio = models.CharField(max_length=20)
    telefono = models.PositiveIntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.correo

class Receta(models.Model):
    telefono = models.PositiveIntegerField()
    correo = models.EmailField()
    def __str__(self):
        return self.correo
