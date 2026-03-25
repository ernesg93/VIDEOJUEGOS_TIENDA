from django.db import models
from django.utils.text import slugify


class Genero(models.Model):
    """Modelo para categorizar videojuegos por género."""
    
    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre del género"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="URL amigable"
    )
    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Visible en filtros"
    )
    
    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ["nombre"]
    
    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class Producto(models.Model):
    """Modelo para videojuegos en el catálogo."""
    
    # Plataformas disponibles
    PLATAFORMA_CHOICES = [
        ("PC", "PC"),
        ("PS5", "PlayStation 5"),
        ("XBOX", "Xbox"),
        ("SWITCH", "Nintendo Switch"),
    ]
    
    # Campos Fase 2.1 (MVP - Must)
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título del juego"
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name="URL amigable"
    )
    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Precio (USD)"
    )
    stock = models.IntegerField(
        default=0,
        verbose_name="Cantidad en inventario"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Visible y disponible para compra"
    )
    
    # Campos Fase 2.2 (Should)
    plataforma = models.CharField(
        max_length=20,
        choices=PLATAFORMA_CHOICES,
        default="PC",
        verbose_name="Plataforma"
    )
    fecha_lanzamiento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de lanzamiento"
    )
    
    # Campos Fase 2.3 (Could)
    descripcion_corta = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Descripción breve"
    )
    descripcion_larga = models.TextField(
        blank=True,
        verbose_name="Descripción detallada"
    )
    genero = models.ForeignKey(
        Genero,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="productos",
        verbose_name="Género"
    )
    
    # Campos Fase 2.4 ( Won't - avanzados)
    precio_oferta = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Precio con descuento"
    )
    edad_minima = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Edad mínima recomendada"
    )
    
    # Metadatos y auditoría
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última modificación"
    )
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)