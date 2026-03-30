from django.core.paginator import Paginator
from django.shortcuts import render

from catalogo.models import Producto
from catalogo.utils import assign_portada_static_path


PLATAFORMA_TERMS = {
    "PC": ["pc", "computadora"],
    "PS5": ["ps5", "playstation", "play station"],
    "XBOX": ["xbox", "xbox series", "series x", "series s"],
    "SWITCH": ["switch", "nintendo switch", "nintendo"],
}


def _extraer_filtro_plataforma(query):
    normalized_query = query.lower().strip()

    for plataforma, terms in PLATAFORMA_TERMS.items():
        for term in terms:
            if term == normalized_query:
                return plataforma, ""

    for plataforma, terms in PLATAFORMA_TERMS.items():
        for term in terms:
            if term in normalized_query:
                remaining_query = normalized_query.replace(term, " ").strip()
                remaining_query = " ".join(remaining_query.split())
                return plataforma, remaining_query

    return "", normalized_query


def resultados_busqueda(request):
    """
    Render search results using a single free-text query.

    Args:
        request: HttpRequest object with the `q` query parameter.

    Returns:
        HttpResponse: Rendered search results page with inferred filters and pagination.
    """
    q = request.GET.get("q", "").strip()

    plataforma_choices = Producto.PLATAFORMA_CHOICES
    plataformas_validas = dict(plataforma_choices)
    plataforma, nombre_query = _extraer_filtro_plataforma(q)

    juegos_qs = Producto.objects.filter(activo=True).order_by("-created_at")

    if nombre_query:
        juegos_qs = juegos_qs.filter(titulo__icontains=nombre_query)

    if plataforma and plataforma in plataformas_validas:
        juegos_qs = juegos_qs.filter(plataforma=plataforma)

    juegos = list(juegos_qs)

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

    pagination_params = request.GET.copy()
    pagination_params.pop("page", None)

    context = {
        "q": q,
        "nombre_query": nombre_query,
        "plataforma": plataforma,
        "plataforma_display": plataformas_validas.get(plataforma, ""),
        "lista_juegos": page_obj,
        "page_obj": page_obj,
        "visible_pages": visible_pages,
        "pagination_query": pagination_params.urlencode(),
    }
    return render(request, "buscador/resultados_busqueda.html", context)
