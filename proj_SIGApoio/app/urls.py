from .views import efetuarChamado, cadastroRecurso, home, cadastroRecurso, cad_local, success_page, cadastroTipoRecurso, reserva_recurso, listar_emprestimos
from django.urls import path

urlpatterns = [
    path('', home, name = 'home'),
    path('recurso/cadastro', cadastroRecurso, name='cadastro-recurso'),
    path('recurso/cadastro-tipo-recurso', cadastroTipoRecurso, name='cadastro-tipo-recurso'),
    path('chamado/efetuar_chamado', efetuarChamado, name='efetuar-chamado'),
    path('cadastro_recurso',cadastroRecurso, name= "cad_recurso"),
    path('cad_local/', cad_local, name = "cad_local"),
    path('success_page/', success_page, name = "success_page"),
    path('reserva_recurso/', reserva_recurso, name='reserva_recurso'),
    path('emprestimos/', listar_emprestimos, name='listar_emprestimos'),
]