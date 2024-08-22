from .views import efetuar_chamado, home, get_locais, cadastro_recurso, cad_local, listar_local, editar_local, remover_local, success_page, cadastro_tipo_recurso, listar_recursos, cadastro_reserva_semanal, tipo_reserva, cadastro_reserva_dia, delete_reserva_dia, delete_reserva_semanal, editar_reserva_semanal, editar_reserva_dia, reserva_recurso, listar_reservas, reserva_details, filtrar_reservas, filtros_reserva, get_locais_dia, listar_emprestimos, recurso_delete, recurso_edit, cadastro_usuario
from django.urls import path, include
from django.contrib.auth.views import LogoutView 

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
    path('success_page/', success_page, name = "success_page"),
    path('reserva_recurso/', reserva_recurso, name='reserva_recurso'),
    path('emprestimos/', listar_emprestimos, name='listar_emprestimos'),
    path('local/listar/', listar_local, name='listar_local'),
    path('local/editar/<int:pk>/', editar_local, name='editar_local'),
    path('local/remover/<int:pk>/', remover_local, name='remover_local'),
    path('local/cadastro', cad_local, name = "cad_local"),
    path('reserva/cadastro/semanal', cadastro_reserva_semanal, name = "cad_reserva_semanal"),
    path('reserva/cadastro/dia', cadastro_reserva_dia, name = "cad_reserva_dia"),
    path('reserva/cadastro/', tipo_reserva, name = "cad_reserva"),
    path('reserva/delete/semanal/<int:id>', delete_reserva_semanal, name = "delete_reserva_semanal"),
    path('reserva/delete/dia/<int:id>', delete_reserva_dia, name = "delete_reserva_dia"),
    path('reserva/editar/semanal/<int:id>', editar_reserva_semanal, name = "editar_reserva_semanal"),
    path('reserva/editar/dia/<int:id>', editar_reserva_dia, name = "editar_reserva_dia"),
    path('get_locais/', get_locais, name = "getLocais"),
    path('get_locais_dia/', get_locais_dia, name = "getLocaisDia"),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('usuarios/registration_form/', cadastro_usuario, name="cadastro_usuario"),
    path('recurso/delete/<int:id>/', recurso_delete, name='rec_delete'),
    path('recurso/edit/<int:id>/', recurso_edit, name='rec_edit')
]