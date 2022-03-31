from django import forms

class UserFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()

class ServiceFormulario(forms.Form):
    numero_cliente = forms.IntegerField()
    nombre_empresa = forms.CharField(max_length=40)
    importe_factura = forms.FloatField()
    vencimiento_factura = forms.DateField()