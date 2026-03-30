from pathlib import Path

from django.contrib.staticfiles import finders


def assign_portada_static_path(producto):
    default_portada = "img/portadas/default.png"
    svg_static_path = Path("img/portadas") / f"{producto.slug}.svg"
    png_static_path = Path("img/portadas") / f"{producto.slug}.png"

    if finders.find(svg_static_path.as_posix()):
        producto.portada_static_path = svg_static_path.as_posix()
    elif finders.find(png_static_path.as_posix()):
        producto.portada_static_path = png_static_path.as_posix()
    else:
        producto.portada_static_path = default_portada

    return producto
