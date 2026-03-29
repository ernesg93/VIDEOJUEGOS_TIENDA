from pathlib import Path

from django.shortcuts import render
from django.contrib.staticfiles import finders

from .models import Producto


def lista_juegos(request):
    """
    Display the active video games catalog with cover fallbacks.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Rendered template with the active games list.
    """
    juegos = list(Producto.objects.filter(activo=True).order_by('-created_at'))
    default_portada = "img/portadas/default.png"

    for juego in juegos:
        svg_static_path = Path("img/portadas") / f"{juego.slug}.svg"
        png_static_path = Path("img/portadas") / f"{juego.slug}.png"

        if finders.find(svg_static_path.as_posix()):
            juego.portada_static_path = svg_static_path.as_posix()
        elif finders.find(png_static_path.as_posix()):
            juego.portada_static_path = png_static_path.as_posix()
        else:
            juego.portada_static_path = default_portada

    context = {
        "lista_juegos": juegos,
    }
    return render(request, "catalogo/lista_juegos.html", context)
