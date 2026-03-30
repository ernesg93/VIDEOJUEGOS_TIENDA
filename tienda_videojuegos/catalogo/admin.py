from django.contrib import admin
from .models import Genero, Producto


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    """Admin interface for Genero model."""
    list_display = ['nombre', 'slug', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre']
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ['activo']
    ordering = ['nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Admin interface for Producto model."""
    list_display = ['titulo', 'precio', 'plataforma', 'stock', 'activo', 'created_at']
    list_filter = ['activo', 'plataforma', 'genero', 'created_at']
    search_fields = ['titulo', 'slug', 'descripcion_corta', 'descripcion_larga']
    prepopulated_fields = {'slug': ('titulo',)}
    list_editable = ['activo', 'stock']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    fieldsets = (
        ('Información básica', {
            'fields': ('titulo', 'slug', 'activo')
        }),
        ('Precio y stock', {
            'fields': ('precio', 'precio_oferta', 'stock')
        }),
        ('Clasificación', {
            'fields': ('plataforma', 'genero', 'edad_minima')
        }),
        ('Contenido', {
            'fields': ('descripcion_corta', 'descripcion_larga')
        }),
        ('Fechas', {
            'fields': ('fecha_lanzamiento', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
