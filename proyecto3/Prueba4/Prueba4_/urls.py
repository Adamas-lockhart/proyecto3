from django.urls import path
from Prueba4_ import views


urlpatterns = [
    path('', views.inicio),
    path('Productos/', views.Producto),
    path('Clientes/', views.Clientes),
    path('ClientesPremiums/', views.Clientes_Premium),
    
]