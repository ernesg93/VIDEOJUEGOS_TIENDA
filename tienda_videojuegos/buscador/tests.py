from django.test import TestCase
from django.urls import reverse

from catalogo.models import Producto


class ResultadosBusquedaViewTests(TestCase):
    def setUp(self):
        Producto.objects.create(
            titulo="The Legend of Zelda: Breath of the Wild",
            precio=59.99,
            plataforma="SWITCH",
            stock=10,
            activo=True,
        )
        Producto.objects.create(
            titulo="Spider-Man 2",
            precio=69.99,
            plataforma="PS5",
            stock=8,
            activo=True,
        )

        Producto.objects.create(
            titulo="Juego Oculto",
            precio=49.99,
            plataforma="PC",
            stock=4,
            activo=False,
        )

    def test_resultados_busqueda_filtra_por_nombre(self):
        response = self.client.get(reverse("buscador:resultados"), {"q": "zelda"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Legend of Zelda: Breath of the Wild")
        self.assertNotContains(response, "Spider-Man 2")

    def test_resultados_busqueda_filtra_por_plataforma(self):
        response = self.client.get(reverse("buscador:resultados"), {"q": "PS5"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Spider-Man 2")
        self.assertNotContains(response, "The Legend of Zelda: Breath of the Wild")

    def test_resultados_busqueda_con_query_vacia_muestra_todos_los_activos(self):
        response = self.client.get(reverse("buscador:resultados"), {"q": "   "})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Legend of Zelda: Breath of the Wild")
        self.assertContains(response, "Spider-Man 2")
        self.assertNotContains(response, "Juego Oculto")

    def test_resultados_busqueda_no_muestra_productos_inactivos(self):
        response = self.client.get(reverse("buscador:resultados"), {"q": "Juego"})

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Juego Oculto")

    def test_resultados_busqueda_muestra_mensaje_si_no_hay_resultados(self):
        response = self.client.get(reverse("buscador:resultados"), {"q": "Metroid"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No se encontraron juegos con esos criterios.")

    def test_resultados_busqueda_combina_nombre_y_plataforma(self):
        response = self.client.get(reverse("buscador:resultados"), {"q": "Spider PS5"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Spider-Man 2")
        self.assertContains(response, "Nombre: spider")
        self.assertContains(response, "Plataforma: PlayStation 5")
        self.assertNotContains(response, "The Legend of Zelda: Breath of the Wild")

    def test_resultados_busqueda_pagina_y_preserva_query_string(self):
        for index in range(7):
            Producto.objects.create(
                titulo=f"Juego Switch {index}",
                precio=39.99 + index,
                plataforma="SWITCH",
                stock=5 + index,
                activo=True,
            )

        response = self.client.get(reverse("buscador:resultados"), {"q": "Switch", "page": 2})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["page_obj"].number, 2)
        self.assertTrue(response.context["page_obj"].has_previous())
        self.assertEqual(response.context["pagination_query"], "q=Switch")
        self.assertContains(response, "?page=1&q=Switch")
