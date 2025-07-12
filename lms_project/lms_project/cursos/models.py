from django.db import models

#? This file defines the models for the LMS project, specifically for courses and lessons.
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()

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
