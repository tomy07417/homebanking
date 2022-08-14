from django.shortcuts import render
from django.http import HttpRequest
from .forms import FormularioRegistro

# Create your views here.

def login(request):
    return render(request, 'login/login.html')

class FormularioRegistroView(HttpRequest):
    def index(request):
        usuario = FormularioRegistro()
        return render(request, 'login/registro.html', {"form": usuario})
    
    def procesar_formulario(request):
        usuario = FormularioRegistro(request.POST)
        if usuario.is_valid():
            usuario.save()
            
            usuario = FormularioRegistro()
            
        return render(request, 'login/registro.html', {"form": usuario,
                                                       "mensaje": "Ok"})