from django.contrib import admin
from .models import Producto, Genero


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre']
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'plataforma', 'precio', 'precio_oferta', 'stock', 'activo', 'created_at']
    list_filter = ['plataforma', 'activo', 'genero', 'created_at']
    search_fields = ['titulo', 'descripcion_corta', 'descripcion_larga']
    prepopulated_fields = {'slug': ('titulo',)}
    readonly_fields = ['created_at', 'updated_at']
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