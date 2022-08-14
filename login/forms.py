from socket import fromshare
from django import forms
from clientes.models import Cliente

class FormularioRegistro(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['customer_name', 'customer_surname', 'customer_DNI', 'dob']