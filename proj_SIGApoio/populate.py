import os
import django

# Defina a variável de ambiente para o arquivo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Configure o Django
django.setup()

# from app import models as md
from app.models import TipoRecurso, Recurso, TipoUsuario, TipoLocal, Local, Horario
import random
from django.contrib.auth.models import User
def generate_schedule():
    schedule = []
    time_slots = {
        'M': {'start': '07:00', 'interval': 50, 'count': 6},
        'T': {'start': '13:00', 'interval': 50, 'count': 6},
        'N': {'start': '18:40', 'interval': 50, 'count': 4},
    }
    days = [2, 3, 4, 5, 6]  # Representa de segunda a sexta
    
    for day in days:
        for shift in time_slots:
            start_time = time_slots[shift]['start']
            interval = time_slots[shift]['interval']
            count = time_slots[shift]['count']
            
            for i in range(1, count + 1):
                id = f"{day}{shift}{i}"
                start_hour, start_minute = map(int, start_time.split(':'))
                if i % 2 == 1 and i != 1:
                    start_minute = start_minute + 10 # Adicionando intervalo
                end_hour = start_hour
                end_minute = start_minute + interval
                if end_minute >= 60:
                    end_hour += end_minute // 60
                    end_minute = end_minute % 60
                
                start_time = f"{start_hour:02}:{start_minute:02}"
                end_time = f"{end_hour:02}:{end_minute:02}"
                schedule.append({
                    'id': id,
                    'dia': day,
                    'horaInicio': start_time,
                    'horaFim': end_time
                })
                
                start_time = end_time  # O próximo horário começa quando esse termina
    
    return schedule

# Gerar horários
horarios = generate_schedule()

# Inserir ou atualizar registros
for horario in horarios:
    Horario.objects.get_or_create(
        id=horario['id'],
        defaults={
            'dia': horario['dia'],
            'horaInicio': horario['horaInicio'],
            'horaFim': horario['horaFim']
        }
    )

# ########################################
# ########################################
# povoando tipos de recursos, tipos de usuarios e tipos de locais

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

###########################
#povoando os recursos
 
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
        
##################################
#povoando as salas
tipo_sala = TipoLocal.objects.get(tipo="Sala")
dados_locais = [
    # Bloco A - salas de 1 a 10
    {"nome": f"Sala A{i}", "bloco": "A", "capacidade": 45, "tipo": tipo_sala} for i in range(1, 11)
] + [
    # Bloco B - salas de 1 a 10, exceto B5
    {"nome": f"Sala B{i}", "bloco": "B", "capacidade": 45, "tipo": tipo_sala} for i in range(1, 11) if i != 5
] + [
    # Bloco D - salas de 1 a 8
    {"nome": f"Sala D{i}", "bloco": "D", "capacidade": 55, "tipo": tipo_sala} for i in range(1, 9)
]

# inserindo dados das salas com loop
for dados in dados_locais:
    Local.objects.get_or_create(
        nome=dados["nome"],
        bloco=dados["bloco"],
        capacidade=dados["capacidade"],
        tipo=dados["tipo"]
    )
    
    
    #################
    #criando superuser
def create_superuser(username,email,password):
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username,email,password)
        print("Tabela Povoada com sucesso")
        print(f"Superuser '{username}' criado com sucesso.")
    else:
        return None
    
if __name__ == "__main__":
    # 'nome','email','senha'
    create_superuser('admin', '', 'admin')