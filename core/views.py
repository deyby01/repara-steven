from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'core/homepage.html')

def sobre_nosotros_view(request):
    return render(request, 'core/sobre_nosotros.html')

def contacto_view(request):
    return render(request, 'core/contacto.html')

def reparaciones_view(request):
    return render(request, 'core/reparaciones.html')