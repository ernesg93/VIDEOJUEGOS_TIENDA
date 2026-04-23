from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class RegistroViewTests(TestCase):
    def test_login_view_returns_ok(self):
        response = self.client.get(reverse("usuarios:login"))

        self.assertEqual(response.status_code, 200)  # type: ignore[attr-defined]
        self.assertTemplateUsed(response, "usuarios/login.html")

    def test_perfil_view_returns_ok_for_authenticated_user(self):
        usuario = User.objects.create_user(username="perfil_user", password="ClaveSegura123!")
        self.client.force_login(usuario)

        response = self.client.get(reverse("usuarios:perfil"))

        self.assertEqual(response.status_code, 200)  # type: ignore[attr-defined]
        self.assertTemplateUsed(response, "usuarios/perfil.html")

    def test_perfil_view_redirects_when_user_is_anonymous(self):
        response = self.client.get(reverse("usuarios:perfil"))

        self.assertRedirects(response, f'{reverse("usuarios:login")}?next={reverse("usuarios:perfil")}')

    def test_login_view_authenticates_user_and_redirects_home(self):
        User.objects.create_user(username="ernesg93", password="ClaveSegura123!")

        response = self.client.post(
            reverse("usuarios:login"),
            {
                "username": "ernesg93",
                "password": "ClaveSegura123!",
            },
        )

        self.assertRedirects(response, reverse("home"))
        self.assertIn("_auth_user_id", self.client.session)

    def test_login_view_shows_error_with_invalid_credentials(self):
        response = self.client.post(
            reverse("usuarios:login"),
            {
                "username": "ernesg93",
                "password": "incorrecta",
            },
        )

        self.assertEqual(response.status_code, 200)  # type: ignore[attr-defined]
        self.assertContains(response, "Usuario o contrasena incorrectos.")
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_logout_view_logs_user_out_and_redirects_login(self):
        usuario = User.objects.create_user(username="logout_user", password="ClaveSegura123!")
        self.client.force_login(usuario)

        response = self.client.get(reverse("usuarios:logout"))

        self.assertRedirects(response, reverse("usuarios:login"))
        self.assertNotIn("_auth_user_id", self.client.session)

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
