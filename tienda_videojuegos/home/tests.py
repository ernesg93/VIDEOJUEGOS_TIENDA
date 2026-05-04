from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class ResponsiveHeaderTemplateTests(TestCase):
    def test_get_home_uses_responsive_zones_with_expected_breakpoints(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)  # type: ignore[attr-defined]
        self.assertContains(response, "navbar-expand-lg")
        self.assertContains(response, "site-header__shell")
        self.assertContains(response, "site-header__topbar")
        self.assertContains(response, "site-header__brand-zone")
        self.assertContains(response, "site-header__desktop-zones d-none d-lg-flex")
        self.assertContains(response, 'id="headerMobileZones"')
        self.assertContains(response, 'data-bs-target="#headerMobileZones"')

    def test_get_home_mobile_panel_keeps_nav_search_user_order(self):
        response = self.client.get(reverse("home"))
        content = response.content.decode()

        nav_index = content.find('site-header__mobile-panel d-lg-none" id="headerMobileZones"')
        self.assertNotEqual(nav_index, -1)
        nav_zone_index = content.find("site-header__nav-zone", nav_index)
        search_zone_index = content.find("site-header__search-zone", nav_index)
        user_zone_index = content.find("site-header__user-zone", nav_index)

        self.assertGreater(nav_zone_index, nav_index)
        self.assertGreater(search_zone_index, nav_zone_index)
        self.assertGreater(user_zone_index, search_zone_index)

    def test_get_home_anonymous_user_menu_shows_login_and_register(self):
        response = self.client.get(reverse("home"))

        self.assertContains(response, "Iniciar Sesion")
        self.assertContains(response, "Registrarse")
        self.assertNotContains(response, "Mi Perfil")
        self.assertNotContains(response, "Cerrar Sesion")

    def test_get_home_authenticated_user_menu_shows_profile_and_logout(self):
        user = User.objects.create_user(username="header_user", password="ClaveSegura123!")
        self.client.force_login(user)

        response = self.client.get(reverse("home"))

        self.assertContains(response, "Mi Perfil")
        self.assertContains(response, "Cerrar Sesion")
        self.assertNotContains(response, "Iniciar Sesion")
        self.assertNotContains(response, "Registrarse")
