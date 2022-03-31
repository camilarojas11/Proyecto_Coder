from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField(primary_key=True)

class Servicio(models.Model):
    numero_cliente = models.IntegerField(primary_key=True)
    nombre_empresa = models.CharField(max_length=40)
    importe_factura = models.FloatField()
    vencimiento_factura = models.DateField()

class PagoDeServicios(models.Model):
    numero_comprobante = models.IntegerField(primary_key=True)
    monto_pagado = models.FloatField()
    fecha_pago = models.DateField()
    check_pago = models.BooleanField()