from pathlib import Path
from unittest.mock import patch

from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from django.urls import reverse

from .admin import ProductoAdmin
from .models import Genero, Producto


class CatalogoViewsContractTests(TestCase):
    def setUp(self):
        self.juego_activo = Producto.objects.create(
            titulo="Halo Infinite",
            precio=59.99,
            stock=8,
            plataforma="XBOX",
            activo=True,
        )
        self.juego_inactivo = Producto.objects.create(
            titulo="Juego Oculto",
            precio=10,
            stock=0,
            plataforma="PC",
            activo=False,
        )

    def test_lista_juegos_renderiza_template_y_contexto_canonico(self):
        response = self.client.get(reverse("catalogo:lista_juegos"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalogo/lista_juegos.html")
        self.assertIn("lista_juegos", response.context)
        self.assertIn("page_obj", response.context)
        self.assertIn("visible_pages", response.context)
        self.assertNotIn("productos", response.context)

    def test_detalle_juego_devuelve_404_si_producto_inactivo(self):
        response = self.client.get(
            reverse("catalogo:detalle_juego", kwargs={"slug": self.juego_inactivo.slug})
        )

        self.assertEqual(response.status_code, 404)

    def test_detalle_juego_renderiza_template_y_contexto_canonico(self):
        response = self.client.get(
            reverse("catalogo:detalle_juego", kwargs={"slug": self.juego_activo.slug})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalogo/detalle_juego.html")
        self.assertIn("juego", response.context)
        self.assertEqual(response.context["juego"].pk, self.juego_activo.pk)

    def test_aliases_de_compatibilidad_reutilizan_contrato_publico(self):
        response_lista = self.client.get(reverse("catalogo:lista_productos"))
        response_detalle = self.client.get(
            reverse("catalogo:detalle_producto", kwargs={"slug": self.juego_activo.slug})
        )

        self.assertEqual(response_lista.status_code, 200)
        self.assertTemplateUsed(response_lista, "catalogo/lista_juegos.html")
        self.assertIn("lista_juegos", response_lista.context)

        self.assertEqual(response_detalle.status_code, 200)
        self.assertTemplateUsed(response_detalle, "catalogo/detalle_juego.html")
        self.assertIn("juego", response_detalle.context)


class CatalogoMigrationContractTests(TestCase):
    def test_0001_initial_permanece_en_baseline_sin_genero_ni_campos_extra(self):
        migration_path = Path(__file__).resolve().parent / "migrations" / "0001_initial.py"
        content = migration_path.read_text(encoding="utf-8")

        self.assertNotIn("name='Genero'", content)
        self.assertNotIn("fecha_lanzamiento", content)
        self.assertNotIn("descripcion_corta", content)
        self.assertNotIn("descripcion_larga", content)
        self.assertNotIn("precio_oferta", content)
        self.assertNotIn("edad_minima", content)

    def test_migracion_incremental_0002_agrega_genero_y_campos_extra(self):
        migration_path = Path(__file__).resolve().parent / "migrations" / "0002_genero_producto_extend.py"
        content = migration_path.read_text(encoding="utf-8")

        self.assertIn("CreateModel", content)
        self.assertIn("name='Genero'", content)
        self.assertIn("AddField", content)
        self.assertIn("fecha_lanzamiento", content)
        self.assertIn("descripcion_corta", content)
        self.assertIn("descripcion_larga", content)
        self.assertIn("precio_oferta", content)
        self.assertIn("edad_minima", content)
        self.assertIn("genero", content)


class CatalogoExtendedDomainTests(TestCase):
    def test_producto_puede_relacionarse_a_genero_y_campos_extra(self):
        genero = Genero.objects.create(nombre="Acción")
        producto = Producto.objects.create(
            titulo="Doom Eternal",
            precio=59.99,
            stock=7,
            plataforma="PC",
            activo=True,
            genero=genero,
            descripcion_corta="FPS frenético",
            descripcion_larga="Demonios, velocidad y heavy metal.",
            precio_oferta=39.99,
            edad_minima=18,
        )

        self.assertEqual(producto.genero.nombre, "Acción")
        self.assertEqual(str(genero), "Acción")
        self.assertEqual(producto.precio_oferta, 39.99)

    def test_producto_no_requiere_campos_extendidos_para_compatibilidad(self):
        producto = Producto.objects.create(
            titulo="Tetris Effect",
            precio=29.99,
            stock=4,
            plataforma="PC",
            activo=True,
        )

        self.assertIsNone(producto.genero)
        self.assertIsNone(producto.fecha_lanzamiento)
        self.assertEqual(producto.descripcion_corta, "")
        self.assertEqual(producto.descripcion_larga, "")
        self.assertIsNone(producto.precio_oferta)
        self.assertEqual(producto.edad_minima, 0)


class CatalogoAdminContractTests(TestCase):
    def test_admin_producto_expone_genero_y_precio_oferta(self):
        self.assertIn("genero", ProductoAdmin.list_display)
        self.assertIn("precio_oferta", ProductoAdmin.list_display)
        self.assertIn("genero", ProductoAdmin.list_filter)
        self.assertIn("genero__nombre", ProductoAdmin.search_fields)


class SeedDataContractTests(TestCase):
    def test_seed_data_es_wrapper_al_management_command(self):
        seed_path = Path(__file__).resolve().parents[2] / "seed_data.py"
        content = seed_path.read_text(encoding="utf-8")

        self.assertIn("call_command", content)
        self.assertIn("populate_productos", content)
        self.assertNotIn("from catalogo.models import Genero", content)

    def test_populate_productos_es_idempotente_y_alinea_datos_existentes(self):
        from catalogo.management.commands.populate_productos import PRODUCTOS

        call_command("populate_productos")
        self.assertEqual(Producto.objects.count(), len(PRODUCTOS))

        juego = Producto.objects.get(titulo="Halo Infinite")
        juego.stock = 0
        juego.activo = False
        juego.save(update_fields=["stock", "activo"])

        call_command("populate_productos")
        juego.refresh_from_db()

        self.assertEqual(Producto.objects.count(), len(PRODUCTOS))
        self.assertEqual(juego.stock, 18)
        self.assertTrue(juego.activo)

    def test_populate_productos_documenta_flujo_canonico(self):
        command_path = Path(__file__).resolve().parent / "management" / "commands" / "populate_productos.py"
        content = command_path.read_text(encoding="utf-8")

        self.assertIn("python manage.py populate_productos", content)
        self.assertIn("seed_data.py", content)

    def test_populate_productos_bloquea_avance_si_0001_no_esta_en_baseline(self):
        contract_drift = "name='Genero'\nfecha_lanzamiento = True"

        with patch("pathlib.Path.read_text", return_value=contract_drift):
            with self.assertRaises(CommandError):
                call_command("populate_productos")

        self.assertEqual(Producto.objects.count(), 0)
