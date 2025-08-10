from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User 
from .models import PerfilUsuario

# Signals to automatically create and save PerfilUsuario when a User is created or updated

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    try:
        instance.perfilusuario.save()
    except PerfilUsuario.DoesNotExist:
        pass
