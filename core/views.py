from django.shortcuts import redirect, render

from core.carrito import Carrito
from core.models import Producto

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def registro(request):
    return render(request, 'core/registro.html')
    
def catalogo(request):
    return render(request, 'core/catalogo.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def iphone14pro(request):
    return render(request, 'core/iphone-14-pro.html')

def galaxys23ultra(request):
    return render(request, 'core/samsung-galaxy-s23-ultra.html')

def carrito(request):
    productos = Producto.objects.all()
    return render(request, 'core/carrito.html',{ 'productos':productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")