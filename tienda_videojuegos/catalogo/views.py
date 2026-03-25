from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Producto, Genero


def lista_productos(request):
    """
    Vista de lista de productos (S2.1).
    Muestra un grid de productos activos.
    Soporta filtros básicos por plataforma (C2.1).
    """
    # Obtener productos activos
    productos = Producto.objects.filter(activo=True).select_related('genero')
    
    # Filtro por plataforma (C2.1 - Could)
    plataforma = request.GET.get('plataforma')
    if plataforma:
        productos = productos.filter(plataforma=plataforma)
    
    # Filtro por género
    genero_slug = request.GET.get('genero')
    if genero_slug:
        productos = productos.filter(genero__slug=genero_slug)
    
    # Obtener géneros activos para el sidebar/filtro
    generos = Genero.objects.filter(activo=True)
    
    context = {
        'productos': productos,
        'generos': generos,
        'plataforma_actual': plataforma,
        'genero_actual': genero_slug,
    }
    return render(request, 'catalogo/lista_productos.html', context)


def detalle_producto(request, slug):
    """
    Vista de detalle de producto (M2.2).
    Muestra información completa del producto.
    """
    producto = get_object_or_404(Producto, slug=slug, activo=True)
    
    # Productos relacionados (mismo género o plataforma)
    relacionados = Producto.objects.filter(
        activo=True
    ).exclude(pk=producto.pk).select_related('genero')[:4]
    
    context = {
        'producto': producto,
        'productos_relacionados': relacionados,
    }
    return render(request, 'catalogo/detalle_producto.html', context)