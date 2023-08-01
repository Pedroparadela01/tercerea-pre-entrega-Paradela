from django import forms

class ProductosForm(forms.Form):
     producto=forms.CharField(max_length=40) 
     precio=forms.CharField(max_length=10)



class EmpleadosForm(forms.Form):
     nombre=forms.CharField(max_length=40)
     apellido=forms.CharField(max_length=40)
     puesto=forms.CharField(max_length=40)


class RepartoForm(forms.Form):
     cliente=forms.CharField(max_length=40) 
     fechaentrega=forms.DateField()
     entregado=forms.BooleanField()
