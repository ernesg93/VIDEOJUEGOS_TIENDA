from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginUsuarioForm, RegistroUsuarioForm

User = get_user_model()


def login_view(request):
    """Handle login form submission and redirect home when authenticated.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Login template or redirect to home when successful.
    """
    if request.method == "POST":
        form = LoginUsuarioForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, "Inicio de sesion correcto.")
            return redirect("home")
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            messages.warning(request, "Completa tu usuario y contrasena para iniciar sesion.")
        elif not User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ingresado no existe.")
        else:
            messages.error(request, "La contrasena ingresada es incorrecta.")
    else:
        form = LoginUsuarioForm(request)

    return render(request, "usuarios/login.html", {"form": form})


@login_required(login_url="usuarios:login")
def perfil_view(request):
    """Render the user profile page placeholder.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Rendered profile template.
    """
    return render(request, "usuarios/perfil.html")


@login_required(login_url="usuarios:login")
def logout_view(request):
    """Log the user out and redirect to login.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponseRedirect: Redirect to login page after logout.
    """
    if request.method != "POST":
        return redirect("usuarios:perfil")

    auth_logout(request)
    messages.success(request, "Sesion cerrada correctamente.")
    return redirect("usuarios:login")


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
