from django.urls import path

from . import views


app_name = "usuarios"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("perfil/", views.perfil_view, name="perfil"),
    path("registro/", views.registro_view, name="registro"),
]
