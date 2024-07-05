from django.contrib import admin
from .models import TipoRecurso, TipoUsuario, Recurso, Usuario, Emprestimo, Horario, Local, Reserva, TipoLocal

admin.site.register(Usuario)
admin.site.register(TipoRecurso)
admin.site.register(TipoUsuario)
admin.site.register(Recurso)
admin.site.register(Emprestimo)
admin.site.register(Horario)
admin.site.register(Local)
admin.site.register(Reserva)

# admin.site.register(TipoLocal)