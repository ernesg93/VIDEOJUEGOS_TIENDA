from django.db import models
from django.utils.text import slugify


class Genero(models.Model):
    """Modelo para categorizar videojuegos por género."""

    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del género")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="URL amigable")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    activo = models.BooleanField(default=True, verbose_name="Visible en filtros")

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.nombre)
            slug = base_slug
            counter = 1

            while Genero.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)


class Producto(models.Model):
    """Modelo para videojuegos en el catálogo."""

    PLATAFORMA_CHOICES = [
        ("PC", "PC"),
        ("PS5", "PlayStation 5"),
        ("XBOX", "Xbox Series X/S"),
        ("SWITCH", "Nintendo Switch"),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título del juego")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="URL amigable")
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio (USD)")
    stock = models.IntegerField(default=0, verbose_name="Stock disponible")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    plataforma = models.CharField(
        max_length=20,
        choices=PLATAFORMA_CHOICES,
        default="PC",
        verbose_name="Plataforma",
    )
    fecha_lanzamiento = models.DateField(null=True, blank=True, verbose_name="Fecha de lanzamiento")
    descripcion_corta = models.CharField(max_length=300, blank=True, verbose_name="Descripción breve")
    descripcion_larga = models.TextField(blank=True, verbose_name="Descripción detallada")
    genero = models.ForeignKey(
        Genero,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="productos",
        verbose_name="Género",
    )
    precio_oferta = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Precio oferta")
    edad_minima = models.IntegerField(null=True, blank=True, verbose_name="Edad mínima recomendada")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-created_at"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            counter = 1
            max_attempts = 100

            while counter < max_attempts:
                if not Producto.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                    self.slug = slug
                    break
                slug = f"{base_slug}-{counter}"
                counter += 1
            else:
                raise ValueError(f"Could not generate unique slug after {max_attempts} attempts")

        super().save(*args, **kwargs)
