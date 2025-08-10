from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Curso
from .forms import UserRegistrationForm, CursoForm
from django.contrib.auth import login   
from .decorators import rol_requerido

#from django.http import HttpResponse

#def vista_inicio(request):
#    return HttpResponse("Bienvenido a mi Sistema de Gestión de Aprendizaje")

def inicio(request):
    return render(request, 'cursos/inicio.html')

@login_required
def lista_cursos(request):
    cursos = Curso.objects.all().order_by('fecha_publicacion')
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})

@login_required
def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    lecciones = curso.lecciones.order_by('orden')  # Usamos el related_name
    return render(request, 'cursos/detalle_curso.html', {'curso': curso, 'lecciones': lecciones})

# This form allows users to register with a username, email, and password.
def registrar_usuario(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserRegistrationForm()
    return render(request, 'cursos/register.html', {'form': form})

@rol_requerido('profesor')
def crear_curso(request):
    return render(request, 'cursos/crear_curso.html')

@rol_requerido('profesor')
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/crear_curso.html', {'form': form})