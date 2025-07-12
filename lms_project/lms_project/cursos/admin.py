from django.contrib import admin
from .models import Curso, Leccion

# Opcional: mostrar las lecciones en línea dentro del curso
class LeccionInline(admin.TabularInline):
    model = Leccion
    extra = 1  # Número de lecciones adicionales en blanco

class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')
    search_fields = ('titulo',)
    inlines = [LeccionInline]  # Lecciones asociadas al curso

class LeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'orden')
    list_filter = ('curso',)
    search_fields = ('titulo',)

admin.site.register(Curso, CursoAdmin)
admin.site.register(Leccion, LeccionAdmin)
