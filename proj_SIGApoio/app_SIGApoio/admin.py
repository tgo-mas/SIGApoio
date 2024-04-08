from django.contrib import admin
from .models import TipoRecurso, TipoUsuario, Recurso, Usuario, Emprestimo

admin.site.register(Usuario)
admin.site.register(TipoRecurso)
admin.site.register(TipoUsuario)
admin.site.register(Recurso)
admin.site.register(Emprestimo)