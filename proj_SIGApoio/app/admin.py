from django.contrib import admin
from .models import TipoRecurso, TipoUsuario, Recurso, Usuario, Emprestimo, Horario, Local, ReservaSemanal, ReservaDiaUnico, TipoLocal, Chamado

admin.site.register(Usuario)
admin.site.register(TipoRecurso)
admin.site.register(TipoUsuario)
admin.site.register(Recurso)
admin.site.register(Emprestimo)
admin.site.register(Horario)
admin.site.register(Local)
admin.site.register(ReservaSemanal)
admin.site.register(ReservaDiaUnico)
admin.site.register(TipoLocal)
admin.site.register(Chamado)

