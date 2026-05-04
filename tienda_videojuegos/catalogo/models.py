from django.db import models
from django.utils.text import slugify


class Genero(models.Model):
    """Clasificación de género para productos del catálogo."""

    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre",
        help_text="Nombre del género del videojuego.",
    )
    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True,
        verbose_name="Slug",
        help_text="Slug autogenerado para URLs legibles.",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

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
    """
    Model representing a video game product in the catalog.
    Phase 2.1 MVP implementation with essential fields.
    """
    PLATAFORMA_PC = 'PC'
    PLATAFORMA_PS5 = 'PS5'
    PLATAFORMA_XBOX = 'XBOX'
    PLATAFORMA_SWITCH = 'SWITCH'

    PLATAFORMA_CHOICES = [
        (PLATAFORMA_PC, 'PC'),
        (PLATAFORMA_PS5, 'PlayStation 5'),
        (PLATAFORMA_XBOX, 'Xbox Series X/S'),
        (PLATAFORMA_SWITCH, 'Nintendo Switch'),
    ]
    
    # Identificación
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name="Slug",
        help_text="Slug autogenerado para la URL pública del producto.",
    )
    
    # Contenido Esencial
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título",
        help_text="Nombre visible del videojuego en catálogo y detalle.",
    )
    
    # Información de Comercio
    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Precio",
        help_text="Precio base del videojuego.",
    )
    stock = models.IntegerField(
        default=0,
        verbose_name="Stock disponible",
        help_text="Cantidad de unidades disponibles para venta.",
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Define si el producto se muestra públicamente en catálogo.",
    )
    
    # Clasificación
    plataforma = models.CharField(
        max_length=20,
        choices=PLATAFORMA_CHOICES,
        verbose_name="Plataforma",
        help_text="Plataforma principal del videojuego.",
    )
    genero = models.ForeignKey(
        Genero,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="productos",
        verbose_name="Género",
        help_text="Género principal del videojuego.",
    )
    fecha_lanzamiento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de lanzamiento",
        help_text="Fecha oficial de lanzamiento del videojuego.",
    )
    descripcion_corta = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name="Descripción corta",
        help_text="Resumen breve para tarjetas y listados.",
    )
    descripcion_larga = models.TextField(
        blank=True,
        default="",
        verbose_name="Descripción larga",
        help_text="Descripción extendida para detalle de producto.",
    )
    precio_oferta = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Precio de oferta",
        help_text="Precio promocional opcional.",
    )
    edad_minima = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Edad mínima",
        help_text="Edad recomendada mínima.",
    )
    
    # Metadatos y Auditoría
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        """
        Generate unique slug from titulo if not provided.
        Uses database queries to check for uniqueness before saving.
        """
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            counter = 1
            max_attempts = 100  # Prevent infinite loops
            
            while counter < max_attempts:
                if not Producto.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                    self.slug = slug
                    break
                slug = f"{base_slug}-{counter}"
                counter += 1
            else:
                raise ValueError(f"Could not generate unique slug after {max_attempts} attempts")
        
        super().save(*args, **kwargs)
