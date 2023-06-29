from django.shortcuts import render
from Prueba4_.models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    inicio = inicio
    return HttpResponse(inicio)

def Producto(request):
    Producto = Producto(nombre = 'manzana', precio = '25', descripcion = 'una rica manzana verde')
    Producto.save()
    Respuesta = f'producto {Producto.nombre} precio {Producto.precio} descripcion {Producto.descripcion}'
    return HttpResponse(Respuesta)

def Clientes(request):
    Nombre = Nombre
    Apellido = Apellido
    Email = Email
    Clientes_ID = Clientes_ID
    Respuesta = f'nombre {Nombre} apellido {Apellido} id {Clientes_ID} Email {Email}'
    return HttpResponse(Respuesta)

def Clientes_Premium(request):
    Nombre = Nombre
    Apellido = Apellido
    Email = Email
    Clientes_ID_Premium = Clientes_ID_Premium
    Respuesta = f'nombre {Nombre} apellido {Apellido} id {Clientes_ID_Premium} Email {Email}'
    return HttpResponse(Respuesta)