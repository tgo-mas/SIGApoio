from .views import efetuar_chamado, home, get_locais, cadastro_recurso, cad_local, listar_local, success_page, cadastro_tipo_recurso, listar_recursos, cadastro_reserva_semanal, tipo_reserva, cadastro_reserva_dia, reserva_recurso, listar_reservas, reserva_details, filtrar_reservas, filtros_reserva, get_locais_dia, listar_emprestimos, cadastrar_emprestimo
from django.urls import path

urlpatterns = [
    path('', home, name = 'home'),
    path('recurso/cadastro', cadastro_recurso, name='cadastro-recurso'),
    path('recurso/cadastro-tipo-recurso', cadastro_tipo_recurso, name='cadastro-tipo-recurso'),
    path('recurso/listar', listar_recursos, name='listar-recurso'),
    path('chamado', efetuar_chamado, name='efetuar-chamado'),
    path('reservas', listar_reservas, name='listar-reservas'),
    path('filtros_reserva', filtros_reserva, name='filtros-reserva'),
    path('lista_filtrada', filtrar_reservas, name='filtrar-reservas'),
    path('reserva_details', reserva_details, name = "reservaDetails"),
    path('cadastro_recurso',cadastro_recurso, name= "cad_recurso"),
    path('cad_local/', cad_local, name = "cad_local"),
    path('success_page/', success_page, name = "success_page"),
    path('reserva_recurso/', reserva_recurso, name='reserva_recurso'),
    path('emprestimos/', listar_emprestimos, name='listar_emprestimos'),
    path('local/listar/', listar_local, name='listar_local'),
    path('local/cad_local', cad_local, name = "cad_local"),
    path('reserva/cadastro/semanal', cadastro_reserva_semanal, name = "cad_reserva_semanal"),
    path('reserva/cadastro/dia', cadastro_reserva_dia, name = "cad_reserva_dia"),
    path('reserva/cadastro/', tipo_reserva, name = "cad_reserva"),
    path('get_locais/', get_locais, name = "getLocais"),
    path('get_locais_dia/', get_locais_dia, name = "getLocaisDia"),
    path('cadastrar-emprestimo/', cadastrar_emprestimo, name='cadastrar_emprestimo') 
    ]