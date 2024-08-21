from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST, require_GET, require_safe, require_http_methods
from .forms import LocalForm, RecursoForm, TipoRecursoForm, ReservaForm, ChamadoForm, ReservaDiaForm, EmprestimoForm, ReservaRecursoForm
from .models import TipoRecurso, Recurso, Local, ReservaSemanal, ReservaDiaUnico, Usuario, Horario, TipoLocal, Chamado, Emprestimo, ReservaRecurso
from .bo.horarios import converter_horarios, converter_horarios_dia, get_horario_at
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.utils import timezone
import json

# @require_GET
def home(request):
    return render(request,'index.html')  

# @require_POST
def cad_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page') 
    else:
        form = LocalForm()
    return render(request, 'local/cad_local.html', {'form': form})


# @require_GET
def success_page(request):
    return render(request, 'local/success_page.html')

# @require_POST
def cadastro_recurso(request):
    if request.method != 'POST':
        form = RecursoForm()
    else:
        form = RecursoForm(request.POST)

        for i in Recurso.objects.all():
            if str(i.tipo) == TipoRecurso.objects.get(pk = form.data['tipo']).tipo and str(i.codigo) == str(form.data['codigo']):
                context = {'erro':'Recurso já cadastrado','form':form}
                return render(request, 'recurso/cadastro_recurso.html', context)
            
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cadastro-recurso'))
        
    context = {'form': form}
    return render(request, 'recurso/cadastro_recurso.html', context)

# @require_POST
def cadastro_tipo_recurso(request):
    if request.method != 'POST':
        form = TipoRecursoForm()
    else:
        form = TipoRecursoForm(request.POST)
        for i in TipoRecurso.objects.all():
            if str(i).lower() == form.data['tipo'].lower():
                context = {'erro':'Tipo de recurso já cadastrado','form':form}
                return render(request, 'recurso/cadastro_tipo_recurso.html', context)
                   
        if form.is_valid():
            form.save()
            return redirect('cadastro-tipo-recurso')
            
    context = {'form':form}
    return render(request, 'recurso/cadastro_tipo_recurso.html', context)

# @require_POST
def reserva_recurso(request):
    tipos_recursos = TipoRecurso.objects.all()
    
    if request.method == 'POST':
        reserva_form = ReservaForm(request.POST)
        if reserva_form.is_valid():
            reserva_form.save()
            return redirect('success_page') 
    else:
        reserva_form = ReservaForm()

    return render(request, 'recurso/reserva_recurso.html', {'reserva_form': reserva_form, 'tipos_recursos': tipos_recursos})

# @require_GET
def listar_emprestimos(request):
    status = request.GET.get('status', '')
    usuario = request.GET.get('usuario', '')
    solicitante = request.GET.get('solicitante', '')

    # Filtragem baseada no status
    emprestimos = Emprestimo.objects.all()

    if status == 'ativos':
        emprestimos = emprestimos.filter(devolvido=False)
    elif status == 'devolvidos':
        emprestimos = emprestimos.filter(devolvido=True)

    # Filtragem por nome de usuário e solicitante
    if usuario:
        emprestimos = emprestimos.filter(matBolsista__nome__icontains=usuario)
    if solicitante:
        emprestimos = emprestimos.filter(matUsuario__nome__icontains=solicitante)

    context = {
        'emprestimos': emprestimos,
        'status': status,
        'usuario': usuario,
        'solicitante': solicitante,
    }
    return render(request, 'emprestimos/lista_emprestimos.html', context)

# @require_GET
def listar_local(request):
    locais = Local.objects.all()
    tipo = request.GET.get('tipo')
    bloco = request.GET.get('bloco')
    capacidade = request.GET.get('capacidade')
    sort = request.GET.get('sort', 'nome')  # Default sort field is 'nome'

    if tipo:
        locais = locais.filter(tipo__tipo=tipo)
    if bloco:
        locais = locais.filter(bloco=bloco)
    if capacidade:
        locais = locais.filter(capacidade=capacidade)

    locais = locais.order_by(sort)

    context = {
        'locais': locais,
        'tipo': tipo,
        'bloco': bloco,
        'capacidade': capacidade,
        'tipos_locais': TipoLocal.objects.all(),
        'sort': sort
    }
    return render(request, 'local/listar_local.html', context)

# @require_GET
def listar_recursos(request):
    recursos = Recurso.objects.all()
    recursos_disponiveis = Recurso.objects.filter(status=True)
    recursos_indisponiveis = Recurso.objects.filter(status=False)
    recursos_funciona = Recurso.objects.filter(funcionando=True)
    recursos_nao_funciona = Recurso.objects.filter(funcionando=False)
    tipos = TipoRecurso.objects.all()
    context = {'recursos':recursos, 'tipos':tipos, 'recursosDisponiveis':recursos_disponiveis, 'recursosIndisponiveis':recursos_indisponiveis, 'recursosNaoFunciona':recursos_nao_funciona, 'recursosFunciona':recursos_funciona}
    return render(request, 'recurso/listar_recurso.html', context)

# @require_GET
def tipo_reserva(request):
    return render(request, 'reserva/tipoReserva.html')

# @require_POST
def cadastro_reserva_semanal(request):
    if request.method != 'POST':
        form = ReservaForm()
        context = {'form': form}
        return render(request, 'reserva/cadastroReserva.html', context)
    else:
        req = request.POST
        form = ReservaForm()
        context = {'form': form, 'message': 'Reserva cadastrada com sucesso!'}
        try:
            descricao = req['descricao']
            resp = Usuario.objects.get(matricula=req['matSolicitante']) # Enquanto a auth não está pronta
            # resp = get_auth_user().get("matricula")                  // Vai ser algo assim depois da autenticação
            solic = Usuario.objects.get(matricula=req['matSolicitante'])
            local = Local.objects.get(id=req['local'])
            horarios_vetor = converter_horarios(req.getlist('dias'), req.getlist('horarios')) # Junta os dias e horarios
            horarios = Horario.objects.filter(id__in=horarios_vetor)
            nova_reserva = ReservaSemanal.objects.create(descricao=descricao, local=local, matResponsavel=resp, matSolicitante=solic)
            nova_reserva.horarios.set(horarios)
            nova_reserva.save()
            return render(request, 'reserva/cadastroReserva.html', context)
        except:
            context = {'form': form, 'message': 'Erro no cadastro da reserva', 'error': True}
            return render(request, 'reserva/cadastroReserva.html', context)
    
# @require_POST
def cadastro_reserva_dia(request):
    if request.method != 'POST':
        form = ReservaDiaForm()
        context = {'form': form }
        return render(request, 'reserva/cadastroReservaDia.html', context)
    else:
        req = request.POST
        form = ReservaDiaForm()
        context = {'form': form, 'message': "Reserva cadastrada com sucesso!"}
        try:
            descricao = req['descricao']
            resp = Usuario.objects.get(matricula=req['matSolicitante']) # Enquanto a auth não está pronta
            # resp = get_auth_user().get("matricula")                  // Vai ser algo assim depois da autenticação
            solic = Usuario.objects.get(matricula=req['matSolicitante'])
            local = Local.objects.get(id=req['local'])
            data_inicio = datetime.strptime(req['diaHoraInicio'], '%Y-%m-%dT%H:%M')    
            data_fim = datetime.strptime(req['diaHoraFim'], '%Y-%m-%dT%H:%M')
            repeticao  = req['repeticao']
            if repeticao == 'unico':
                nova_reserva = ReservaDiaUnico.objects.create(descricao=descricao,
                                                         local=local, 
                                                         diaHoraInicio=data_inicio, 
                                                         diaHoraFim=data_fim,
                                                         matResponsavel=resp, 
                                                         matSolicitante=solic)
                nova_reserva.save()
            elif repeticao == 'semana':
                while data_inicio.year == datetime.now().year:
                    nova_reserva = ReservaDiaUnico.objects.create(descricao=descricao,
                                                         local=local, 
                                                         diaHoraInicio=data_inicio, 
                                                         diaHoraFim=data_fim,
                                                         matResponsavel=resp, 
                                                         matSolicitante=solic)
                    nova_reserva.save()
                    data_inicio = data_inicio + timedelta(weeks=1)  # Pula uma semana
                    data_fim = data_fim + timedelta(weeks=1)
            elif repeticao == 'mes':
                while data_inicio.year == datetime.now().year:
                    nova_reserva = ReservaDiaUnico.objects.create(descricao=descricao,
                                                         local=local, 
                                                         diaHoraInicio=data_inicio, 
                                                         diaHoraFim=data_fim,
                                                         matResponsavel=resp, 
                                                         matSolicitante=solic)
                    nova_reserva.save()
                    data_inicio = data_inicio + relativedelta(months=1)  # Pula um mês
                    data_fim = data_fim + relativedelta(months=1)
            
            return render(request, 'reserva/cadastroReservaDia.html', context)
        except Exception as error:
            context = {'form': form, 'message': 'Erro no cadastro da reserva', 'error': True}
            print(error)
            return render(request, 'reserva/cadastroReservaDia.html', context)
      
# @require_POST
@csrf_exempt
def get_locais(request):
    data = json.loads(request.body)
    horarios = data['horarios']
    dias = data['dias']
    bloco = data['bloco']
    pessoas = data['pessoas']
    horarios_final = converter_horarios(dias, horarios)
    reservas_filt = ReservaSemanal.objects.filter(
        Q(horarios__id__in=horarios_final)
    )
    locais_ocupados = map(lambda reserva: reserva.local, reservas_filt)
    locais = Local.objects.exclude(
        Q(nome__in=locais_ocupados)
    )
    locais_final = locais.filter(
        capacidade__gt=pessoas,
        bloco=bloco
    )
    context = {'locais':locais_final}
    return render(request, 'reserva/local_option.html', context)

# @require_POST
def efetuar_chamado(request):
    if request.method != 'POST':
        form = ChamadoForm()
    else:
        form = ChamadoForm(request.POST)
        #print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('efetuar-chamado'))
        
    context = {'form': form}
    return render(request, 'reserva/efetuar_chamado.html', context)

# @require_GET
def listar_reservas(request):
    filtro_tipo='default'

    try:
        request.GET.get('filtro_tipo')
    except:
        filtro_tipo = 'default'

    context = {"filtro_tipo": filtro_tipo}

    return render(request, "reserva/listar_reservas.html", context)

# @require_GET
def filtros_reserva(request):
    filtro = request.GET.get('filtro')
    context = {'filtro': filtro}

    return render(request, "reserva/filtros_reserva.html", context)

# @require_GET
def filtrar_reservas(request):
    filtro_tipo = request.GET.get('filtro_tipo')
    filtro_local = request.GET.get('filtro_local')
    filtro_resp = request.GET.get('filtro_resp')
    reservas_s = ReservaSemanal.objects.all()
    reservas_d = ReservaDiaUnico.objects.all()

    reservas = []
    for res in reservas_d:
        reservas.append(res)
    for res in reservas_s:
        reservas.append(res)

    context = {"reservas": reservas,
               "filtro_tipo": filtro_tipo,
               "filtro_local": filtro_local,
               "filtro_resp": filtro_resp}

    return render(request, "reserva/lista_filtrada.html", context)

# @require_GET
@csrf_exempt
def reserva_details(request):
    reserva_detail = None
    
    reserva_pk = request.GET.get('reserva_pk')
    reserva_tipo = request.GET.get('reserva_tipo')

    if (reserva_tipo == 'S'):
        reserva_detail = ReservaSemanal.objects.get(pk=reserva_pk)
    elif (reserva_tipo == 'D'):
        reserva_detail = ReservaDiaUnico.objects.get(pk=reserva_pk)

    context = {'reserva': reserva_detail}
    return render(request, 'reserva/reserva_details.html', context)
    

# @require_POST
@csrf_exempt
def get_locais_dia(request):
    data = json.loads(request.body)
    dia = data['diaInicio']
    diaFim = data['diaFim']
    bloco = data['bloco']
    pessoas = data['pessoas']
    print(dia, diaFim)
    horarios_final = converter_horarios_dia(dia, diaFim)
    
    if horarios_final is None:      ## se horarios_final for None, pule a verificação com os horarios da semana
        lista_reservas = []
    else:
        reservas_filt = ReservaSemanal.objects.filter(
            Q(horarios__id__in=horarios_final)
        )
        lista_reservas = list(reservas_filt)
    
    lista_reservas += list(ReservaDiaUnico.objects.filter(
                          diaHoraInicio__range=[dia, diaFim]
                      ))
    
    locais_ocupados = map(lambda reserva: reserva.local, lista_reservas)
    locais = Local.objects.exclude(
        Q(nome__in=locais_ocupados)
    )
    locais_final = locais.filter(
        capacidade__gt=pessoas,
        bloco=bloco
    )
    context = {'locais':locais_final}
    return render(request, 'reserva/local_option.html', context)

def cadastrar_emprestimo(request):
    print("View cadastrar_emprestimo foi chamada")

    if request.method == 'POST':
        print("Método POST foi detectado")
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            print("Formulário válido")

            try:
                recurso_id = form.cleaned_data['idRecurso'].id_codigo  
                idRecurso = Recurso.objects.get(id_codigo=recurso_id)
                matBolsista = form.cleaned_data['matBolsista'].matricula
                matUsuario = form.cleaned_data['matUsuario'].matricula

                print(f"idRecurso: {idRecurso}, matBolsista: {matBolsista}, matUsuario: {matUsuario}")

                # Como `horaEntrada` já é um datetime, não é necessário convertê-lo
                data_hora = form.cleaned_data['horaEntrada']
                
                print(f"Data e Hora recebidas: {data_hora}")

                # Determinação do dia da semana (1 = segunda-feira, 7 = domingo)
                dia_semana = data_hora.weekday() + 1

                print(f"Dia da semana: {dia_semana}")

                # Verificação de horários compatíveis
                hora_obj = data_hora.time()
                horario = Horario.objects.filter(
                    dia=dia_semana, 
                    horaInicio__lte=hora_obj, 
                    horaFim__gte=hora_obj
                ).first()

                print(f"Horário selecionado: {horario}")

                if horario:
                    # Criação do objeto Empréstimo
                    emprestimo = Emprestimo(
                        idRecurso=idRecurso,  
                        matBolsista=Usuario.objects.get(matricula=matBolsista),
                        matUsuario=Usuario.objects.get(matricula=matUsuario),
                        horaEntrada=datetime.combine(data_hora.date(), horario.horaInicio),
                    )
                    emprestimo.save()

                    print("Empréstimo salvo com sucesso!")

                    return redirect('cadastrar_emprestimo')
                else:
                    form.add_error(None, "Nenhum horário disponível para o período selecionado.")
                    print("Nenhum horário compatível encontrado.")
            except Exception as e:
                form.add_error(None, f"Erro ao cadastrar o empréstimo: {e}")
                print(f"Erro ao tentar cadastrar o empréstimo: {e}")
        else:
            form.add_error(None, "Formulário inválido. Verifique os campos.")
            print("Formulário inválido.")
    else:
        form = EmprestimoForm()

    return render(request, 'recurso/reserva_recurso.html', {'reserva_form': form})


from django.contrib import messages

def cadastrar_reserva_recurso(request):
    if request.method == 'POST':
        form = ReservaRecursoForm(request.POST)
        if form.is_valid():
            idRecurso = form.cleaned_data['idRecurso']
            docente = form.cleaned_data['docente']
            dia = form.cleaned_data['dia']
            horaInicio = form.cleaned_data['horaInicio']
            horaFim = form.cleaned_data['horaFim']

            # Verifica se já existe uma reserva com os mesmos parâmetros
            reserva_existente = ReservaRecurso.objects.filter(
                idRecurso=idRecurso,
                dia=dia,
                horaInicio=horaInicio,
                horaFim=horaFim
            ).exists()

            if reserva_existente:
                messages.error(request, "Recurso já reservado para este horário")
            else:
                form.save()
                messages.success(request, "Reserva cadastrada com sucesso!")
                return redirect('cadastrar_reserva_recurso') 
    else:
        form = ReservaRecursoForm()
    
    return render(request, 'recurso/cadastro_reserva_recurso.html', {'reserva_form': form})

def excluir_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    if request.method == 'POST':
        emprestimo.delete()
        messages.success(request, 'Empréstimo excluído com sucesso.')
        return redirect('emprestimos/lista_emprestimos')  # Redirecionar para a lista de empréstimos
    return render(request, 'emprestimos/confirmar_exclusao.html', {'emprestimo': emprestimo})



def editar_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empréstimo editado com sucesso!')
            return redirect('listar_emprestimos')  # Redirecionar para a lista de empréstimos
    else:
        form = EmprestimoForm(instance=emprestimo)
    return render(request, 'emprestimos/editar_emprestimo.html', {'form': form})


def registrar_devolucao(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    if not emprestimo.devolvido:  # Verifica se o empréstimo ainda não foi devolvido
        emprestimo.devolvido = True
        emprestimo.horaEntrada = timezone.now()  # Define a hora da devolução
        emprestimo.save()
    return redirect('listar_emprestimos')  # Redireciona para a página de listagem de empréstimos