from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        help_text="Nombre del género del videojuego.",
                        max_length=100,
                        unique=True,
                        verbose_name="Nombre",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        help_text="Slug autogenerado para URLs legibles.",
                        max_length=120,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Última actualización"),
                ),
            ],
            options={
                "verbose_name": "Género",
                "verbose_name_plural": "Géneros",
                "ordering": ["nombre"],
            },
        ),
        migrations.AddField(
            model_name="producto",
            name="descripcion_corta",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Resumen breve para tarjetas y listados.",
                max_length=255,
                verbose_name="Descripción corta",
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="descripcion_larga",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Descripción extendida para detalle de producto.",
                verbose_name="Descripción larga",
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="edad_minima",
            field=models.PositiveSmallIntegerField(
                default=0,
                help_text="Edad recomendada mínima.",
                verbose_name="Edad mínima",
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="fecha_lanzamiento",
            field=models.DateField(
                blank=True,
                help_text="Fecha oficial de lanzamiento del videojuego.",
                null=True,
                verbose_name="Fecha de lanzamiento",
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="genero",
            field=models.ForeignKey(
                blank=True,
                help_text="Género principal del videojuego.",
                null=True,
                on_delete=models.SET_NULL,
                related_name="productos",
                to="catalogo.genero",
                verbose_name="Género",
            ),
        ),
        migrations.AddField(
            model_name="producto",
            name="precio_oferta",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Precio promocional opcional.",
                max_digits=8,
                null=True,
                verbose_name="Precio de oferta",
            ),
        ),
    ]
