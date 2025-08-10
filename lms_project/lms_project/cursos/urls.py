from django.urls import path # type: ignore
from django.contrib.auth import views as auth_views
from . import views

# URL patterns for the cursos app
# This file defines the URL routing for the cursos app, including paths for user registration, login, logout, and course management.
# It maps URLs to their corresponding view functions, allowing users to interact with the LMS system.
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='cursos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
]