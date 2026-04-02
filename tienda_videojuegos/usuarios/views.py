from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render

from .forms import RegistroUsuarioForm


def login_view(request):
    """Render the login page placeholder.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Rendered login template.
    """
    return render(request, "usuarios/login.html")


def perfil_view(request):
    """Render the user profile page placeholder.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Rendered profile template.
    """
    return render(request, "usuarios/perfil.html")


def registro_view(request):
    """Handle user registration, log the user in and redirect home.

    Args:
        request: HttpRequest object with registration form data.

    Returns:
        HttpResponse: Registration page or redirect to home when successful.
    """
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            auth_login(request, usuario)
            messages.success(request, "Tu cuenta fue creada correctamente. Ya iniciaste sesion.")
            return redirect("home")
    else:
        form = RegistroUsuarioForm()

    return render(request, "usuarios/registro.html", {"form": form})
