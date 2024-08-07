from django import template
from ..models import TipoRecurso, Recurso, Local, ReservaSemanal, ReservaMensal, ReservaDiaUnico, Usuario, Horario, TipoLocal, Chamado
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="to_int")
def to_int(value):
    return int(value)

@register.filter(name="to_str")
def to_str(value):
    return str(value)

@register.filter(name="detalhar")
def detalhar(reserva):
    result = ""
    if isinstance(reserva, ReservaDiaUnico):
        result = """
        <div>
            <div>%s</div>
            <div>%s</div>
            <div>%s</div>
            <div>%s</div>
            <div>%s</div>
            <div>%s</div>
        </div> 
        """ %(reserva.descricao, reserva.diaHoraInicio, reserva.diaHoraFim, reserva.local, reserva.matResponsavel, reserva.matSolicitante)

    elif isinstance(reserva, ReservaSemanal):
        chamados = Chamado.objects.filter(reserva=reserva)
        result = f"""
        <div>
            <div>{reserva.descricao}</div>
            <div>{reserva.horarios}</div>
            <div>{reserva.local}</div>
            <div>{reserva.matResponsavel}</div>
            <div>{reserva.matSolicitante}</div>"""
        for chamado in chamados:
            result += f"<div>{chamado}</div>"
        result += "</div>"
    
    return mark_safe(result)