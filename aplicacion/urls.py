from django.urls import path, include
from .views import *
from .forms import *

urlpatterns = [
    path('', index, name="inicio"),

    path('empleados/', empleados , name="empleados"),
    path('productos/', productos, name="productos"),
    path('reparto/', reparto , name="reparto"),
    path('reparto_form/', repartoform, name="reparto_form" ) , 
    path('empleados_form/', empleadosform, name="empleados_form" ) ,
    path('productos_form/', productoform, name="productos_form" ),  
    path('buscar_producto/', buscarProducto, name="buscar_producto/" ),
    path('buscar2/', buscar2, name="buscar2/" ),

 ]   
