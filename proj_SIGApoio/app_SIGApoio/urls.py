from .views import efetuarChamado, cadastroRecurso, home
from django.urls import path

urlpatterns = [
    path('', home, name = 'home'),
    path('recurso/cadastro', cadastroRecurso, name='cadastro-recurso'),
    path('chamado/efetuar_chamado', efetuarChamado, name='efetuar-chamado'),
]