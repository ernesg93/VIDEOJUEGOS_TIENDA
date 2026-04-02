from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class RegistroViewTests(TestCase):
    def test_login_view_returns_ok(self):
        response = self.client.get(reverse("usuarios:login"))

        self.assertEqual(response.status_code, 200)  # type: ignore[attr-defined]
        self.assertTemplateUsed(response, "usuarios/login.html")

    def test_perfil_view_returns_ok(self):
        response = self.client.get(reverse("usuarios:perfil"))

        self.assertEqual(response.status_code, 200)  # type: ignore[attr-defined]
        self.assertTemplateUsed(response, "usuarios/perfil.html")

    def test_registro_view_creates_user_and_logs_in(self):
        response = self.client.post(
            reverse("usuarios:registro"),
            {
                "username": "nuevo_usuario",
                "email": "nuevo@email.com",
                "password1": "ClaveSegura123!",
                "password2": "ClaveSegura123!",
            },
        )

        self.assertRedirects(response, reverse("home"))
        self.assertTrue(User.objects.filter(username="nuevo_usuario").exists())
        self.assertIn("_auth_user_id", self.client.session)
