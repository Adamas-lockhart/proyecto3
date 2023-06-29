from django.db import models

# Create your models here.

class Inicio(models.Model):
    inicio = models.CharField(("Bienvenidos"), max_length=50)

class Producto(models.Model):
    Nombre = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Descripcion = models.TextField()
    
    def __str__(self):
        return self.Nombre

class Clientes(models.Model):
    Cliente_ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=75)
    Apellido = models.CharField(max_length=75)
    Email = models.EmailField(max_length=254)
    Telefono = models.CharField( max_length=50)
    Direccion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Nombre

class Clientes_Premium(Clientes):
    cliente = models.OneToOneField(Clientes, on_delete=models.CASCADE)
    Cliente_ID_Premium = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.Nombre