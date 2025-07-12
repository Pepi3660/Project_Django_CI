from django.shortcuts import render, get_object_or_404
from .models import Curso

#from django.http import HttpResponse

#def vista_inicio(request):
#    return HttpResponse("Bienvenido a mi Sistema de Gestión de Aprendizaje")

def inicio(request):
    return render(request, 'cursos/inicio.html')

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    lecciones = curso.lecciones.order_by('orden')  # Usamos el related_name
    return render(request, 'cursos/detalle_curso.html', {'curso': curso, 'lecciones': lecciones})