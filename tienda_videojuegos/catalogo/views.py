from pathlib import Path

from django.core.paginator import Paginator
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

    paginator = Paginator(juegos, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    current_page = page_obj.number
    page_range_start = max(current_page - 2, 1)
    page_range_end = min(current_page + 2, paginator.num_pages)
    visible_pages = range(page_range_start, page_range_end + 1)

    context = {
        "lista_juegos": page_obj,
        "page_obj": page_obj,
        "visible_pages": visible_pages,
    }
    return render(request, "catalogo/lista_juegos.html", context)
