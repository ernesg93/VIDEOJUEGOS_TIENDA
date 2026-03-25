from django.shortcuts import render
from .models import Producto


def lista_juegos(request):
    """
    View function to display a list of video games.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse: Rendered template with games list
    """
    juegos = Producto.objects.filter(activo=True).order_by('-created_at')
    context = {
        "lista_juegos": juegos,
    }
    return render(request, "catalogo/lista_juegos.html", context)
