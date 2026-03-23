from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    # Lista de productos (S2.1) - accessible en /catalogo/
    path('', views.lista_productos, name='lista_productos'),
    
    # Detalle de producto (M2.2) - accessible en /producto/<slug:slug>/
    path('producto/<slug:slug>/', views.detalle_producto, name='detalle_producto'),
]