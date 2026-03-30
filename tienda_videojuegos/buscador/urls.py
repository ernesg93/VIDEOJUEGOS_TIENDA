from django.urls import path

from .views import resultados_busqueda

app_name = "buscador"

urlpatterns = [
    path("", resultados_busqueda, name="resultados"),
]
