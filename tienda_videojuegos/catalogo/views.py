from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Producto
from .utils import assign_portada_static_path


def lista_juegos(request):
    """
    Display the active video games catalog with cover fallbacks.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Rendered template with the active games list.
    """
    juegos = list(Producto.objects.filter(activo=True).order_by('-created_at'))

    for juego in juegos:
        assign_portada_static_path(juego)

    paginator = Paginator(juegos, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    current_page = page_obj.number
    total_pages = len(paginator.page_range)
    page_range_start = max(current_page - 2, 1)
    page_range_end = min(current_page + 2, total_pages)
    visible_pages = range(page_range_start, page_range_end + 1)

    context = {
        "lista_juegos": page_obj,
        "page_obj": page_obj,
        "visible_pages": visible_pages,
    }
    return render(request, "catalogo/lista_juegos.html", context)


def detalle_juego(request, slug):
    """
    Display the detail page for one active video game.

    Args:
        request: HttpRequest object.
        slug: Unique slug for the selected product.

    Returns:
        HttpResponse: Rendered template with the product detail.
    """
    juego = get_object_or_404(Producto, slug=slug, activo=True)
    assign_portada_static_path(juego)

    context = {
        "juego": juego,
    }
    return render(request, "catalogo/detalle_juego.html", context)
