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
