from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from core.carrito import Carrito
from core.models import Producto

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def registro(request):
    return render(request, 'core/registro.html')
    
def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'core/catalogo.html',{'productos':productos})

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

def gestionarproductos(request):
    productoslista = Producto.objects.all()
    return render(request, 'core/gestionarproductos.html',{ 'productoslista':productoslista})

def registrarEquipo(request):
    nombre = request.POST['txtNombre']
    categoria = request.POST['txtCategoria']
    precio = request.POST['txtPrecio']

    equipo = Producto.objects.create(nombre=nombre, categoria=categoria, precio=precio)
    return redirect('/gestionarproductos/')

def eliminarEquipo(request, nombre):
    equipo = Producto.objects.get(nombre=nombre)
    equipo.delete()
    return redirect('/gestionarproductos/')

def edicionEquipo(request,nombre):
    equipo = Producto.objects.get(nombre=nombre)
    return render(request, "edicionEquipo.html", {"equipo": equipo})

def editarEquipo(request):
    nombre = request.POST['txtNombre']
    categoria = request.POST['txtCategoria']
    precio = request.POST['txtPrecio']

    equipo = Producto.objects.get(nombre=nombre)
    equipo.nombre = nombre
    equipo.categoria = categoria
    equipo.precio = precio

    equipo.save()

    return redirect('/gestionarproductos/')

def loginSession(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username=="j.riquelmee" and password=="pass1234":
            request.session["user"] = username
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/crud.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"pages/login.html",context)
    else:
        context = {

        }
        return render(request,"pages/login.html",context)