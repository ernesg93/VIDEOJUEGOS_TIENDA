from django.contrib import admin

from .models import Genero, Producto


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    """Admin interface for Genero model."""

    list_display = ["nombre", "slug", "created_at"]
    search_fields = ["nombre", "slug"]
    prepopulated_fields = {"slug": ("nombre",)}
    ordering = ["nombre"]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Admin interface for Producto model."""

    list_display = [
        "titulo",
        "genero",
        "precio",
        "precio_oferta",
        "plataforma",
        "stock",
        "activo",
        "created_at",
    ]
    list_filter = ["activo", "plataforma", "genero", "created_at"]
    search_fields = ["titulo", "slug", "genero__nombre"]
    prepopulated_fields = {"slug": ("titulo",)}
    list_editable = ["activo", "stock"]
    ordering = ["-created_at"]
