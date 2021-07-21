from django.db import models

class Patient_History(models.Model):
    Fecha_de_Ingreso = models.DateTimeField()
    Paciente_ID = models.CharField(max_length=64)
    Nombre_y_Apellido = models.CharField(max_length=100)
    Fecha_de_Nacimiento = models.DateTimeField()
    Sexo = models.CharField(max_length=100)
    Edad = models.CharField(max_length=100)
    Estado_civil = models.CharField(max_length=100)
    Teléfono = models.CharField(max_length=100)
    Correo_Electrónico = models.CharField(max_length=100)
    Grupo_Sanguineo = models.CharField(max_length=100)
    Dirección = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=100)
    Alergias_a_medicamentos = models.CharField(max_length=100)
    Enfermedades_que_padece = models.CharField(max_length=100)
    Enfermedades_preexistentes = models.CharField(max_length=100)
    Profesión_y_Ocupación = models.CharField(max_length=100)
    Razón_de_la_Consulta = models.CharField(max_length=100)

class Paciente_Acceso_Rápido (models.Model):
    Paciente_ID = models.ForeignKey(Patient_History, on_delete=models.CASCADE, related_name="identificación")
    Nombre_y_Apellido = models.ForeignKey(Patient_History, on_delete=models.CASCADE, related_name="nombre")
    Teléfono = models.CharField(max_length=100)
    Correo_Electrónico = models.CharField(max_length=100)
    Razón_de_Consulta = models.CharField(max_length=200)

class Nueva_Consulta (models.Model):
    Nombre_y_Apellido = models.CharField(max_length=100)
    Fecha = models.DateTimeField()
    Motivo_Consulta = models.CharField(max_length=100)
    APP = models.CharField(max_length=100)
    AQ = models.CharField(max_length=100)
    A_Medicamentos = models.CharField(max_length=100)

class Generar_Receta (models.Model):
    Nombre_y_Apellido = models.CharField(max_length=100)
    Fecha = models.DateTimeField()
    Prescripciónes = models.CharField(max_length=300)
    Indicaciones = models.CharField(max_length=300)

class Datos_Del_Equipo (models.Model):
    Descripción = models.CharField(max_length=300)
    Modelo = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
    Serie = models.CharField(max_length=300)
    Numero_de_Orden_del_Equipo = models.CharField(max_length=100)
    Estado_del_Equipo = models.CharField(max_length=300)
    Fecha_de_Adquisición = models.DateTimeField()
    Fecha_de_Instalación = models.DateTimeField()
    Precio_Total = models.CharField(max_length=100)
    Observaciones = models.CharField(max_length=400)


class Mantenimiento_y_Contacto_del_Equipo (models.Model):
    Fecha_de_Inicio = models.DateTimeField()
    Frecuencia_de_Mantenimiento  = models.CharField(max_length=100)
    Garantía = models.CharField(max_length=100)
    Número_de_Contrato  = models.CharField(max_length=100)
    Vigencia_del_Contrato  = models.CharField(max_length=100)
    Nivel_de_Riesgo  = models.CharField(max_length=100)
    Prioridad_del_Equipo  = models.CharField(max_length=100)
    Nombre_del_Proveedor_Responsable  = models.CharField(max_length=100)
    Nombre_del_Contacto  = models.CharField(max_length=100)
    Teléfono_del_Contacto  = models.CharField(max_length=100)
    Email_del_Contacto  = models.CharField(max_length=100)

class Crear_Cita (models.Model):
    Nombre_y_Apellido = models.CharField(max_length=100)
    Fecha = models.DateTimeField()
    Especialidad =  models.CharField(max_length=100)
