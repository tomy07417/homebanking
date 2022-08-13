from turtle import onclick
from django.db import models

# Create your models here.
class Cliente(models.Model):
    customer_id = models.AutoField(primary_key= True)
    customer_name = models.CharField(max_length= 255)
    customer_surname = models.CharField(max_length= 255)
    customer_DNI = models.CharField(max_length= 9)
    dob = models.CharField(max_length= 10)
    branch_id = models.ForeignKey("sucursales.Sucursal", on_delete= models.CASCADE)
    direcciones_id = models.ForeignKey("sucursales.SujetoDireccion", on_delete= models.CASCADE)
