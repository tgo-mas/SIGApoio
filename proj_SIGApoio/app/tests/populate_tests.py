import os, sys
import django
from django.core.management import execute_from_command_line
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.models import TipoRecurso, Recurso, TipoUsuario, TipoLocal, Local, Horario
import random
from django.contrib.auth.models import User

tipo_recursos = [
    'HDMI',
    'Projetor',
    'Notebook'
]
tipo_usuarios = [
    "Bolsista",
    "Servidor",
    "Docente",
]

tipo_local =[
    "Sala",
    "Laboratório",
    "Auditório"
]

for tipo in tipo_local:
    TipoLocal.objects.get_or_create(tipo=tipo)
    
for tipo in tipo_recursos:
    TipoRecurso.objects.get_or_create(tipo=tipo)
    
for tipo in tipo_usuarios:
    TipoUsuario.objects.get_or_create(tipo=tipo)

tipo_recursos_get = {
    "HDMI": TipoRecurso.objects.get(tipo="HDMI"),
    "Projetor": TipoRecurso.objects.get(tipo="Projetor"),
    "Notebook": TipoRecurso.objects.get(tipo="Notebook")
}

id_codigo_counter = 1
for tipo_nome, tipo_recurso in tipo_recursos_get.items():
    for i in range(10):
        Recurso.objects.get_or_create(
            id_codigo=id_codigo_counter,
            defaults={
                'codigo': 1000 + id_codigo_counter,
                'tipo': tipo_recurso,
                'status': random.choice([True, False]),  # Aleatoriamente True ou False
                'funcionando': random.choice([True, False])  # Aleatoriamente True ou False
            }
        )
        id_codigo_counter += 1
        
tipo_sala = TipoLocal.objects.get(tipo="Sala")
dados_locais = [
    {"nome": f"Sala A{i}", "bloco": "A", "capacidade": 45, "tipo": tipo_sala} for i in range(1, 11)
] + [
    {"nome": f"Sala B{i}", "bloco": "B", "capacidade": 45, "tipo": tipo_sala} for i in range(1, 11) if i != 5
] + [
    {"nome": f"Sala D{i}", "bloco": "D", "capacidade": 55, "tipo": tipo_sala} for i in range(1, 9)
]

for dados in dados_locais:
    Local.objects.get_or_create(
        nome=dados["nome"],
        bloco=dados["bloco"],
        capacidade=dados["capacidade"],
        tipo=dados["tipo"]
    )
    
    
def create_superuser(username,email,password):
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username,email,password)
        print("Tabela Povoada com sucesso")
        print(f"Superuser '{username}' criado com sucesso.")
    else:
        return None
    
if __name__ == "__main__":
    create_superuser('admin', '', 'admin')