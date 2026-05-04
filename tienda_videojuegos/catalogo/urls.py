from django.urls import path

from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.lista_juegos, name='lista_juegos'),
    path('lista/', views.lista_productos, name='lista_productos'),
    path('producto/<slug:slug>/', views.detalle_producto, name='detalle_producto'),
    path('<slug:slug>/', views.detalle_juego, name='detalle_juego'),
]
