from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('registro', registro, name='registro'),
    path('catalogo/', catalogo, name='catalogo'),
    path('iphone-14-pro/', iphone14pro, name='iphone14pro'),
    path('samsung-galaxy-s23-ultra/', galaxys23ultra, name='galaxys23ultra'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contacto/', contacto, name='contacto'),
]