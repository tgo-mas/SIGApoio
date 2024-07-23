from .views import efetuarChamado, cadastroRecurso, home, cadastroRecurso, cad_local, success_page, cadastroTipoRecurso, listarRecursos, cadastroReserva
from django.urls import path

urlpatterns = [
    path('', home, name = 'home'),
    path('recurso/cadastro', cadastroRecurso, name='cadastro-recurso'),
    path('recurso/cadastro-tipo-recurso', cadastroTipoRecurso, name='cadastro-tipo-recurso'),
    path('recurso/listar', listarRecursos, name='listar-recurso'),
    path('chamado/efetuar_chamado', efetuarChamado, name='efetuar-chamado'),
    path('local/cad_local', cad_local, name = "cad_local"),
    path('reserva/cadastroReserva', cadastroReserva, name = 'cadastro-reserva')
]