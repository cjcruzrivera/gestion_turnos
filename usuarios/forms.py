from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.password_validation import validate_password

from .models import Usuario


class UsuarioForm(UserCreationForm):
    error_messages = {
        'duplicate_username': 'Nombre de usuario ya en uso. Ingrese otro',
        'password_mismatch': "Los dos passwords no coinciden.",
    }
    class Meta:
        model = Usuario

        fields = ['username', 'first_name', 'last_name',
                  'fecha_nacimiento', 'rol', 'sucursal', 'email']

        labels = {
            'username': 'Código',
            'first_name': 'Nombre/s',
            'last_name': 'Apellidos',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'rol': 'Cargo',
            'sucursal': 'Sucursal',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'codigo', 'placeholder': 'Ingrese el codigo del empleado'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre', 'placeholder': 'Ingrese el nombre del empleado'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'apellidos', 'placeholder': 'Ingrese los apellidos del empleado'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'id': 'fecha_nacimiento', 'placeholder': 'Ingrese la fecha de nacimiento del empleado'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Ingrese el correo electronico'}),
            'rol': forms.Select(attrs={'class': 'form-control', 'id': 'rol', 'placeholder': 'Seleccione el cargo del empleado'}),
            'sucursal': forms.Select(attrs={'class': 'form-control', 'id': 'sucursal', 'placeholder': 'Seleccione la sucursal del empleado'}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'id': 'tipo', 'placeholder': 'Seleccione el cargo del empleado'}),
        }

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            Usuario._default_manager.get(username=username)
            # if the user exists, then let's raise an error message

            raise forms.ValidationError(
                # user my customized error message
                self.error_messages['duplicate_username'],

                code='duplicate_username',  # set the error message key

            )
        except Usuario.DoesNotExist:
            return username  # great, this user does not exist so we can continue the registration process

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        validate_password(password1)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
