from .views import cadastroRecurso, home, cadastroTipoRecurso
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', home, name = 'home'),
    path('recurso/cadastro', cadastroRecurso, name='cadastro-recurso'),
    path('recurso/cadastro-tipo', cadastroTipoRecurso, name='cadastro-tipo-recurso')
]