from .views import efetuarChamado, cadastroRecurso, home, getLocais, getLocaisDia, cadastroRecurso, cad_local, listar_local, success_page, cadastroTipoRecurso, listarRecursos, cadastroReservaSemanal, tipoReserva, cadastroReservaDia, cadastroReservaMensal, reserva_recurso
from django.urls import path

urlpatterns = [
    path('', home, name = 'home'),
    path('recurso/cadastro', cadastroRecurso, name='cadastro-recurso'),
    path('recurso/cadastro-tipo-recurso', cadastroTipoRecurso, name='cadastro-tipo-recurso'),
    path('recurso/listar', listarRecursos, name='listar-recurso'),
    path('chamado/efetuar_chamado', efetuarChamado, name='efetuar-chamado'),
    path('cadastro_recurso',cadastroRecurso, name= "cad_recurso"),
    path('cad_local/', cad_local, name = "cad_local"),
    path('success_page/', success_page, name = "success_page"),
    path('reserva_recurso/', reserva_recurso, name='reserva_recurso'),
    path('local/listar/', listar_local, name='listar_local'),
    path('local/cad_local', cad_local, name = "cad_local"),
    path('reserva/cadastro/semanal', cadastroReservaSemanal, name = "cad_reserva_semanal"),
    path('reserva/cadastro/dia', cadastroReservaDia, name = "cad_reserva_dia"),
    path('reserva/cadastro/mensal', cadastroReservaMensal, name = "cad_reserva_mensal"),
    path('reserva/cadastro/', tipoReserva, name = "cad_reserva"),
    path('get_locais/', getLocais, name = "getLocais"),
    path('get_locais_dia/', getLocaisDia, name = "getLocaisDia"),
]