from django.contrib import admin
from .models import Empleados, Reparto , Productos

# Register your models here.

admin.site.register(Empleados)
admin.site.register(Reparto)
admin.site.register(Productos)

