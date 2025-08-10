from django.http import HttpResponseForbidden
from django.shortcuts import redirect   
from functools import wraps 

def rol_requerido(rol_requerido):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
           if not request.user.is_authenticated:
                return redirect('login')
           if request.user.perfilusuario.rol != rol_requerido:
               return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
           return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
