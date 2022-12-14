from django.shortcuts import render
from .forms import FormularioPrestamo
from .models import Prestamo
from cliente.models import Cuenta

# Create your views here.
def prestamos(request):
    cuenta = request.user.cliente.idcuenta
    form = FormularioPrestamo(request.POST)
    LIMITE = {'C': 100000, 
              'G': 300000,
              'B': 500000}
    
    if form.is_valid():
        if int(request.POST.get("monto")) <= LIMITE[cuenta.tipo_cuenta]:
            prestamo = Prestamo(monto=request.POST.get("monto"),
                                tipo_prestamo=request.POST.get("tipo_prestamo"),
                                fecha_inicio=request.POST.get("fecha_inicio"),
                                cuenta=cuenta)
            prestamo.save()
        
            cuenta = Cuenta.objects.get(id_cuenta=cuenta.id_cuenta)
            cuenta.saldo += int(prestamo.monto)
            cuenta.save()
            
            form = FormularioPrestamo()
        
        else:
            form = FormularioPrestamo()
            return render(request, 'prestamo/prestamo.html', {"form": form,
                                                            "mensaje": "error"})
    
    else:
        form = FormularioPrestamo()
        
    return render(request, 'prestamo/prestamo.html', {"form": form})