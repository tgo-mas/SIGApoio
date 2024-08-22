from app.models import Horario
from django.db.models import Q
from datetime import datetime, time

def get_str_horarios(horarios):
    horarios_obj = converter_horarios_back(horarios)
    str_horarios = ''
    for dia in horarios_obj['dias']:
        str_horarios += dia
    for horario in horarios_obj['horarios']:
        if horario[0] not in str_horarios:
            str_horarios += horario
        else:
            str_horarios += horario[1]
    return str_horarios

def converter_horarios(dias, horarios):
    '''Converte 2 vetores de strings, um de dias e outro de horarios, em apenas horarios com seus respectivos dias'''
    horarios_final = []
    for dia in dias:
        for horario in horarios:
            horarios_final.append(dia + horario)
    return horarios_final
    
def converter_horarios_back(horarios):
    '''Converte 1 vetor de strings, com os horários e seus respectivos códigos, em 2 vetores: dias e horarios'''
    horarios_final = []
    dias_final = []
    for horario in horarios:
        dia = horario[0]
        if dia not in dias_final:
            dias_final.append(dia)
            
        horario_obj = horario[1:]
        if horario_obj not in horarios_final:
            horarios_final.append(horario_obj)
    
    return {'horarios': horarios_final, 'dias': dias_final}
            

def converter_horarios_dia(data_inicio, data_final):
    '''Recebe duas datas e retorna os horarios entre elas.'''
    dia_hora_inicio = datetime.strptime(data_inicio, '%Y-%m-%dT%H:%M')    
    dia_hora_final = datetime.strptime(data_final, '%Y-%m-%dT%H:%M')
    
    dia_semana_inicio = dia_hora_inicio.weekday() ## 0 - Segunda, 6 - domingo
    dia_semana_final = dia_hora_final.weekday()
    
    if dia_semana_inicio == 6:
        dia_semana_inicio = 0 
    else:
        dia_semana_inicio = dia_semana_inicio + 1 ## segunda = 1 e assim em diante
    
    if dia_semana_final == 6:
        dia_semana_final = 0 
    else:
        dia_semana_final = dia_semana_final + 1
        
    if dia_semana_inicio in [6, 0] and dia_semana_final in [6, 0]: ## se começar e terminar no fim de semana, retorna None
        return None
    
    horario_inicio = get_horario_at(dia_semana_inicio, f'{dia_hora_inicio.hour:02d}:{dia_hora_inicio.minute:02d}', True)
    horario_final = get_horario_at(dia_semana_final, f'{dia_hora_final.hour:02d}:{dia_hora_final.minute:02d}', False)
    
    horarios_final = get_horarios_between(horario_inicio, horario_final)
    return horarios_final
    
def get_horario_at(dia_semana, hora, inicio):
    if dia_semana in [6, 0] and inicio: ## se começar no final de semana, pula pra segunda
        dia_semana = 1
    elif dia_semana in [6, 0] and not inicio: ## se terminar no final de semana, antecipa pra sexta
        dia_semana = 5
        
    hora_obj = time.fromisoformat(hora)
    horarios = Horario.objects.filter(
        dia=dia_semana,
        horaInicio__lte=hora_obj, 
        horaFim__gte=hora_obj
    )
    horario = horarios.first()
    if horario != None:
        return horario
    else:
        horario = Horario.objects.filter(
            dia=dia_semana,
            horaInicio__gt=hora_obj
        ).order_by('horaInicio').first()
        return horario
    
def get_horarios_between(horario_inicio, horario_final):
    dia_inicio = horario_inicio.dia
    dia_fim = horario_final.dia
    hora_inicio = horario_inicio.horaInicio
    hora_fim = horario_final.horaFim
    
    if dia_inicio == dia_fim:
        horarios = Horario.objects.filter(
            dia=dia_inicio,
            horaInicio__lte=hora_fim,
            horaFim__gte=hora_inicio
        )
    else:
        # Condição para horários entre dias diferentes
        horarios = Horario.objects.filter(
            (Q(dia=dia_inicio) & Q(horaInicio__gte=hora_inicio)) |  # dia = dia inicio e horaInicio >= hora_inicio
            (Q(dia__gt=dia_inicio) & Q(dia__lt=dia_fim)) | # dia > dia_inicio e dia < dia_fim
            (Q(dia=dia_fim) & Q(horaFim__lte=hora_fim)) # dia = dia_fim e horaFim <= hora_fim
        )
    
    return horarios
