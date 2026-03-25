from django.db import models
from django.utils.text import slugify


class Producto(models.Model):
    """
    Model representing a video game product in the catalog.
    Phase 2.1 MVP implementation with essential fields.
    """
    PLATAFORMA_CHOICES = [
        ('PC', 'PC'),
        ('PS5', 'PlayStation 5'),
        ('XBOX', 'Xbox Series X/S'),
        ('SWITCH', 'Nintendo Switch'),
    ]
    
    # Identificación
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    # Contenido Esencial
    titulo = models.CharField(max_length=200, verbose_name="Título")
    
    # Información de Comercio
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(default=0, verbose_name="Stock disponible")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    # Clasificación
    plataforma = models.CharField(
        max_length=20,
        choices=PLATAFORMA_CHOICES,
        verbose_name="Plataforma"
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
