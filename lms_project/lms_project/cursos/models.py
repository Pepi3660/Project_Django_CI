from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

#? This file defines the models for the LMS project, specifically for courses and lessons.
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    imagen = models.ImageField(upload_to='cursos_media/', blank=True, null=True)
    def __str__(self):
        return self.titulo

#? The Leccion model represents lessons within a course.
#? It has a foreign key relationship with the Curso model, allowing multiple lessons to be associated with a single course.
class Leccion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='lecciones')
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    orden = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.orden}. {self.titulo}"

#? The PerfilUsuario model extends the User model to include additional fields specific to the LMS application.

class PerfilUsuario(models.Model):
    ROLES = (
        ('estudiante', 'Estudiante'),
        ('profesor', 'Profesor'),
        ('administrador', 'Administrador'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.user.username} - {self.rol}"
