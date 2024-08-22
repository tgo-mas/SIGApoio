from django import template
from ..models import TipoRecurso, Recurso, Local, ReservaSemanal, ReservaDiaUnico, Usuario, Horario, TipoLocal, Chamado
from django.utils.safestring import mark_safe
from django.urls import reverse
from ..bo.horarios import get_str_horarios

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
            <div>Descrição: %s</div>
            <div>Início: %s</div>
            <div>Final: %s</div>
            <div>Local: %s</div>
            <div>Responsável: %s</div>
            <div>Solicitante: %s</div>
        </div> 
        """ %(reserva.descricao, reserva.diaHoraInicio, reserva.diaHoraFim, reserva.local, reserva.matResponsavel, reserva.matSolicitante)

    elif isinstance(reserva, ReservaSemanal):
        chamados_vetor = Chamado.objects.filter(reserva=reserva)
        horarios_vetor = reserva.horarios.values_list()
        horarios = map(
            lambda horario: horario[0],
            horarios_vetor
        )
        str_horarios = get_str_horarios(horarios)
        
        # for chamado in chamados:
        #     print(chamado)

        result = f"""
        <div>
            <div>Descrição: {reserva.descricao}</div>
            <div>Local: {reserva.local}</div>
            <div>Horário: {str_horarios}</div>
            <div>Responsável: {reserva.matResponsavel}</div>
            <div>Solicitante: {reserva.matSolicitante}</div>"""
        # for chamado in chamados:
        #     result += f"<div>{chamado}</div>"
        # result += "</div>"
    
    return mark_safe(result)

@register.filter(name="criar_filtro")
def criar_filtro(valor):
    if valor == "1":
        result = ""
    elif valor == "2":
        result = """
            <select class="form-select" aria-label="Default select example" name="tipo_reserva" id='filtro_tipo_reserva' >
                <option selected value="default">------------</option>
                <option value="S">Semanal</option>
                <option value="D">Dia Unico</option>
            </select>
        """
    elif valor == "3":
        res_d = ReservaDiaUnico.objects.all()
        res_s = ReservaSemanal.objects.all()

        locais = []
        for res in res_d:
            if res.local not in locais:
                locais.append(res.local)
        for res in res_s:
            if res.local not in locais:
                locais.append(res.local)

        result = """
            <select class="form-select" aria-label="Default select example" name="local_reserva" id="filtro_local_reserva">
                <option selected value="default">------------</option>"""
        
        for local in locais:
            result += "<option value='%d'>%s</option>" %(local.pk, local)
        
        result += "</select>"

    elif valor == "4":
        res_d = ReservaDiaUnico.objects.all()
        res_s = ReservaSemanal.objects.all()

        resps = []
        for res in res_d:
            if res.matResponsavel not in resps:
                resps.append(res.matResponsavel)
        for res in res_s:
            if res.matResponsavel not in resps:
                resps.append(res.matResponsavel)

        result = """
           <select class="form-select" aria-label="Default select example" name="resp_reserva" id="filtro_resp_reserva">
                <option selected value="default">------------</option>"""
        for resp in resps:
            result += "<option value='%d'>%s</option>" %(resp.pk, resp.nome)
        
        result += "</select>"
    else:
        result = ""

    return mark_safe(result)

@register.filter(name="get_tipo_reserva")
def get_tipo_reserva(reserva):
    if isinstance(reserva, ReservaDiaUnico):
        stipo = 'D'
    elif isinstance(reserva, ReservaSemanal):
        stipo = 'S'
    else:
        stipo = "M"
    return stipo

@register.filter(name="linha_tabela")
def linha_tabela(reserva):
    
    if isinstance(reserva, ReservaDiaUnico):
        tipo = "Dia Único"
        delete_url = reverse('delete_reserva_dia', kwargs={'id': reserva.pk})
        edit_url = reverse('editar_reserva_dia', kwargs={'id': reserva.pk})
    elif isinstance(reserva, ReservaSemanal):
        tipo = "Semanal"
        delete_url = reverse('delete_reserva_semanal', kwargs={'id': reserva.pk})
        edit_url = reverse('editar_reserva_semanal', kwargs={'id': reserva.pk})
    else:
        tipo = "undefined"
        
    stipo = get_tipo_reserva(reserva)

    result = f"""
        <tr>
            <td scope="row">{reserva.pk}</td>
            <td>{tipo}</td>
            <td>{reserva.local}</td>
            <td>{reserva.matResponsavel.nome}</td>
            <td>
                <a class='reserva' name='reserva' tipoR='{stipo}' idReserva='{reserva.pk}'><button class="btn btn-primary btn-sm me-1"><i class="bi bi-list-columns-reverse"></i></button></a>
                <button class="btn btn-primary btn-sm me-1"><a style="color: white" href="{edit_url}"><i class="bi bi-pencil-square"></i></a></button>
                <button id="deletebtn_{stipo}_{reserva.pk}" onClick="openDeleteModal(event)" delete_url={delete_url} class="btn btn-danger btn-sm"><i class="bi bi-trash"></i></button>
            </td>
        </tr>
    """

    return mark_safe(result)