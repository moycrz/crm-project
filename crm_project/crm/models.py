from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)

class Contacto(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class EjecutivoCuenta(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    ejecutivo = models.ForeignKey(EjecutivoCuenta, on_delete=models.CASCADE)

class Lead(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=[
        ('Cliente Potencial', 'Cliente Potencial'),
        ('Propuesta en Curso', 'Propuesta en Curso'),
        ('Cliente Potencial Asegurado', 'Cliente Potencial Asegurado'),
        ('Propuesta Enviada', 'Propuesta Enviada'),
        ('Cerrado', 'Cerrado'),
    ])
    ejecutivo = models.ForeignKey(EjecutivoCuenta, on_delete=models.CASCADE)

class OportunidadVenta(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_cierre = models.DateField()

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

class Tarea(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    asignado_a = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField()
