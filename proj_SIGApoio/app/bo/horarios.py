from app.models import Horario
from django.db.models import Q
from datetime import datetime, time

def converter_horarios(dias, horarios):
    '''Converte 2 vetores de strings, um de dias e outro de horarios, em apenas horarios com seus respectivos dias'''
    horarios_final = []
    for dia in dias:
        for horario in horarios:
            horarios_final.append(dia + horario)
    return horarios_final
 
def getHorarioAt(diaSemana, hora, inicio):
    if diaSemana in [6, 0] and inicio: ## se começar no final de semana, pula pra segunda
        diaSemana = 1
    elif diaSemana in [6, 0] and not inicio: ## se terminar no final de semana, antecipa pra sexta
        diaSemana = 5
        
    hora_obj = time.fromisoformat(hora)
    horarios = Horario.objects.filter(
        dia=diaSemana,
        horaInicio__lte=hora_obj, 
        horaFim__gte=hora_obj
    )
    horario = horarios.first()
    if horario != None:
        return horario
    else:
        horario = Horario.objects.filter(
            dia=diaSemana,
            horaInicio__gt=hora_obj
        ).order_by('horaInicio').first()
        return horario
    
def getHorariosBetween(horarioInicio, horarioFinal):
    dia_inicio = horarioInicio.dia
    dia_fim = horarioFinal.dia
    hora_inicio = horarioInicio.horaInicio
    hora_fim = horarioFinal.horaFim
    
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