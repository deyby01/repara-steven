from django.shortcuts import render, get_object_or_404 
from .models import Producto

# Create your views here.
def lista_equipos(request):
    productos = Producto.objects.filter(disponible=True).order_by('-fecha_creacion')
    context = {
        'productos': productos
    }
    return render(request, 'tienda/lista_equipos.html', context)

def detalle_equipo(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, disponible=True)
    context = {
        'producto': producto
    }
    return render(request, 'tienda/detalle_equipo.html', context)