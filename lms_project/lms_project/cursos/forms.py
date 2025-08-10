from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilUsuario, Curso   


# lms_project/lms_project/cursos/forms.py
# This file contains forms related to user registration and profile management.
# It includes a custom user registration form that extends Django's UserCreationForm. 

class UserRegistrationForm(UserCreationForm):
    rol = forms.ChoiceField(choices=PerfilUsuario.ROLES, required=True, label="rol")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'rol')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            perfil = user.perfilusuario
            perfil.rol = self.cleaned_data['rol']
            perfil.save()
        return user

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descripcion', 'fecha_publicacion', 'imagen']
