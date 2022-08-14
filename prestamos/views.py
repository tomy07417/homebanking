from datetime import timezone
from django.shortcuts import render
from .forms import PrestamosForm
from django.shortcuts import redirect

# Create your views here.
def prestamos(request):
    forms = PrestamosForm()
    return render(request, 'Prestamos/prestamos.html', {'forms': forms})

# ADAPTAR ESTO PARA PRESTAMOS
def post_new(request):
    if request.method == "POST":
        form = PrestamosForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save() 
            return redirect('post_detail', pk=post.pk)
    else:
        forms = PrestamosForm()
    return render(request, 'Prestamos/prestamos.html', {'forms': forms})
