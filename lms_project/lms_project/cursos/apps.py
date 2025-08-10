from django.apps import AppConfig


class CursosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cursos'

    def ready(self):
        import cursos.signals  # Import signals to ensure they are registered
        # This ensures that the signals are connected when the app is ready.
        cursos.signals
