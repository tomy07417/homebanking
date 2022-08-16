from django.db import models

# Create your models here.
class Cliente(models.Model):
    #usuario = models.OneToOneField(User, on_delete= models.CASCADE)
    customer_id = models.AutoField(primary_key= True)
    customer_name = models.CharField(max_length= 255)
    customer_surname = models.CharField(max_length= 255)
    customer_DNI = models.CharField(max_length= 9)
    dob = models.CharField(max_length= 10)
    direcciones_id = models.ForeignKey("Direcciones", on_delete= models.CASCADE)

class Direcciones (models.Model):
    idDireccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    provincia = models.CharField (max_length=255)
    pais = models.CharField(max_length=255)