from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class LoginUsuarioForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de usuario", "autofocus": True}
        ),
    )
    password = forms.CharField(
        label="Contrasena",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Contrasena"}
        ),
    )


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Correo electronico",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "tu@email.com"}
        ),
    )

    class Meta(UserCreationForm.Meta):  # type: ignore[misc]
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre de usuario"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Nombre de usuario"
        self.fields["password1"].label = "Contrasena"
        self.fields["password2"].label = "Confirmar contrasena"
        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Contrasena",
                "autocomplete": "new-password",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Repite la contrasena",
                "autocomplete": "new-password",
            }
        )
