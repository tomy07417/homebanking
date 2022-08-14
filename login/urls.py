from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name= 'login'),
    path('registro/', views.FormularioRegistroView.index, name= 'registrarUsuario'),
    path('guardarUsuario/', views.FormularioRegistroView.procesar_formulario, name= 'guardarUsuario')
]