from django.db import models

# Create your models here.

class Disposditivo_Medico(models.Model):
    descripción = models.CharField(max_length=200)
    Modelo = models.CharField(max_length=200)
    Marca = models.CharField(max_length=200)
    Serie = models.CharField(max_length=200)
    Numero_de_Orden_del_Equipo = models.CharField(max_length=200)
    Estado  = models.CharField(max_length=200)
    Fecha_de_Adquisición =models.DateTimeField('date adquisision')
    Fecha_de_Instalación =models.DateTimeField('date instalation')
    Precio_total =models.CharField(max_length=200)
    Observaciones =models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
