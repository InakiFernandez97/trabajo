from django.shortcuts import render

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