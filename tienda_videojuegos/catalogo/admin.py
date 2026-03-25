from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Admin interface for Producto model."""
    list_display = ['titulo', 'precio', 'plataforma', 'stock', 'activo', 'created_at']
    list_filter = ['activo', 'plataforma', 'created_at']
    search_fields = ['titulo', 'slug']
    prepopulated_fields = {'slug': ('titulo',)}
    list_editable = ['activo', 'stock']
    ordering = ['-created_at']
