from django import template
from ..models import TipoRecurso, Recurso, Local, ReservaSemanal, Usuario, Horario, TipoLocal, ReservaDiaUnico, Emprestimo
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="filtro_tipo")
def filtro_tipo(recurso, tipo):
        
    if recurso.status:
        status = 'Disponivel'
    else:
        status = 'Indisponível'
        
    if recurso.funcionando:
        funcionando = 'sim'
    else:
        funcionando = 'nao'
    
    if recurso.tipo.tipo == tipo:
        result = """
                <tr>
                    <th scope="row"> %d</th>
                    <td>%d</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>""" %(recurso.id_codigo, recurso.codigo, tipo, status, funcionando)
        print('testando')
    else:
        result = ''
    return mark_safe(result)