"""Wrapper explícito para poblar catálogo vía management command."""

import os

import django
from django.core.management import call_command


def cargar_datos():
    """Delega la carga de seed al comando Django canónico e idempotente."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tienda_videojuegos.settings")
    django.setup()
    call_command("populate_productos")


if __name__ == "__main__":
    cargar_datos()
