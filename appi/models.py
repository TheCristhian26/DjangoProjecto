from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tipo_persona(models.Model):
    nombre=models.CharField(max_length=100)

class Persona(models.Model):
    codigo = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length= 20, blank= False, null= False)
    tipoPersona = models.ForeignKey(tipo_persona, on_delete=models.CASCADE,default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

class producto(models.Model):
    nombre_produto=models.CharField(max_length=100)
    persona=models.ForeignKey(Persona, on_delete=models.CASCADE,default=1)



class ventas(models.Model):
    numero_ventas=models.BigIntegerField()
    numero_de_factura=models.BigIntegerField()
    estado_factura=models.BooleanField(default=True)
    fecha=models.DateTimeField(auto_now_add=True)
    producto1=models.ForeignKey(producto, on_delete=models.CASCADE,default=1)
    persona=models.ForeignKey(Persona, on_delete=models.CASCADE,default=1)
    

class usuario(models.Model):
    persona= models.OneToOneField(Persona, on_delete=models.CASCADE)
    username= models.CharField(max_length=100)
    password=models.CharField(max_length= 20, blank= False, null= False)




