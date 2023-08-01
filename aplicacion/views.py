from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

from .models import * 

# Create your views here.

def index(request):
    return render(request, "aplicacion/index.html")

def empleados(request):
    ctx = {"empleados": Empleados.objects.all()}
    return render(request, "aplicacion/empleados.html",ctx)

def productos(request):
    ctx = {"productos": Productos.objects.all()}
    return render(request, "aplicacion/productos.html",ctx)

def reparto(request):
    ctx = {"reparto": Reparto.objects.all()}
    return render(request, "aplicacion/reparto.html",ctx)

#forms

def productoform(request):
    if request.method == "POST":
        miForm = ProductosForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            producto = Productos(producto=informacion["producto"], precio=informacion["precio"])
            producto.save() 
            return render(request, "aplicacion/index.html")
    else: 
        miForm= ProductosForm()
    return render(request, "aplicacion/productos_form.html", {"form":miForm})



def empleadosform(request):
    if request.method == "POST":
        miForm = EmpleadosForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            empleado = Empleados(nombre=informacion["nombre"], apellido=informacion["apellido"],puesto=informacion["puesto"])
            empleado.save() 
            return render(request, "aplicacion/index.html")
    else: 
        miForm= EmpleadosForm()
    return render(request, "aplicacion/empleados_form.html", {"form":miForm})



def repartoform(request):
    if request.method == "POST":
        miForm = RepartoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            reparto = Reparto(cliente=informacion["cliente"], fechaentrega=informacion["fechaentrega"],entregado=informacion["entregado"])
            reparto.save() 
            return render(request, "aplicacion/index.html")
    else: 
        miForm= RepartoForm()
    return render(request, "aplicacion/reparto_form.html", {"form":miForm})

def buscarProducto(request):
    return render(request, "aplicacion/buscarProducto.html")

def buscar2(request):
    if request.GET['producto']:
        productosb = request.GET['producto']
        productos = Productos.objects.filter(producto__icontains=productosb)
        return render(request, "aplicacion/resultadoProducto.html", {"productos": productos})
    return HttpResponse ("No se han ingresado datos de busqueda ")
    
    

