from django.urls import path, include
from .views import *
from core import views

urlpatterns = [
    path('', index, name='index'),
    path('registro', registro, name='registro'),
    path('catalogo/', catalogo, name='catalogo'),
    path('iphone-14-pro/', iphone14pro, name='iphone14pro'),
    path('samsung-galaxy-s23-ultra/', galaxys23ultra, name='galaxys23ultra'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('carrito/', carrito, name='carrito'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('gestionarproductos/', gestionarproductos, name='gestionarproductos')
]