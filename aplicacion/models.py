from django.db import models

# Create your models here.

class Empleados(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    puesto=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido}" 

class Productos(models.Model):
    producto=models.CharField(max_length=40) 
    precio=models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.producto}"


class Reparto(models.Model):
    cliente=models.CharField(max_length=40) 
    fechaentrega=models.DateField()
    entregado=models.BooleanField()


    def __str__(self):
        return f"Reparto: {self.cliente}"