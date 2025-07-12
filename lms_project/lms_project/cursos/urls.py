from django.urls import path
from . import views

# URL patterns for the cursos app
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
]