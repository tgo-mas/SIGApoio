from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from rolepermissions.checkers import has_permission
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views.decorators.http import require_POST, require_GET, require_safe, require_http_methods
from .forms import LocalForm, RecursoForm, TipoRecursoForm, ReservaForm, ChamadoForm, ReservaDiaForm
from .models import TipoRecurso, Recurso, Local, ReservaSemanal, ReservaDiaUnico, Usuario, Horario, TipoLocal, Chamado, Emprestimo
from .bo.horarios import converter_horarios, converter_horarios_dia, converter_horarios_back
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from rolepermissions.roles import assign_role
import json
from django.contrib import messages
from django.utils import timezone


# @require_GET
def home(request):
    return render(request,'index.html')  


from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView
)
from django.shortcuts import redirect, render




def cadastro_usuario(request):
    if autenticar_permissao(request,'cadastrar_usuario') is not True:
        return autenticar_permissao(request,'cadastrar_usuario')
    if request.method == "GET":
        return render(request, 'registration/registration_form.html')
    else:
        username= request.POST.get ('username')
        email_cad= request.POST.get ('email')
        confirma_email= request.POST.get('confirm_email')
        senha = request.POST.get ('password')
        confirma_senha = request.POST.get ('confirm_password') 
        tipo_usuario = request.POST.get ('tipo_usuario')
        print(tipo_usuario)
        
        user = User.objects.filter(username=username).first()
        email = User.objects.filter(email=email_cad).first()
        
        if user:
            return HttpResponse("Já existe usuario cadastrado")
        if email:
            return HttpResponse("Já existe login com esse e-mail")
        if confirma_senha != senha:
            return HttpResponse("As senhas não coincidem")
        if confirma_email != email_cad:
            return HttpResponse("E-mails diferentes")
        else:
            user = User.objects.create_user(username= username, email=email_cad, password=senha)
            user.save()
            assign_role(user,tipo_usuario)
            return HttpResponseRedirect(reverse('home'))
            
def login(request):
    if request.method== "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha =  request.POST.get('password')
        user = User.objects.filter(username=username).first()
        user= authenticate(username= username, password= senha)
        if user:
            login_django(request, user)
            return HttpResponse('autenticado')
        else:
            print("n achou")
            return HttpResponse('Não tá autenticado')

                



# @require_POST
def cad_local(request):
    if autenticar_permissao(request,'cadastrar_local') is not True:
        return autenticar_permissao(request,'cadastrar_local')
    if request.method == 'POST':
        form = LocalForm()
    else:
        form = LocalForm(request.POST)

        # Verificar se o local já existe
        nome_local = form.data.get('nome')  # Assumindo que 'nome' é o campo que identifica o local
        if Local.objects.filter(nome=nome_local).exists():
            context = {'erro': 'Esse local já existe!', 'form': form}
            return render(request, 'local/cad_local.html', context)

        # Se o formulário é válido, salvar o novo local
        if form.is_valid():
            form.save()
            messages.success(request, 'Local foi cadastrado com sucesso!')
            return HttpResponseRedirect(reverse('cad_local'))

    context = {'form': form}
    return render(request, 'local/cad_local.html', context)



# @require_GET
def success_page(request):
    return render(request, 'local/success_page.html')

# @require_POST
def cadastro_recurso(request):
    if autenticar_permissao(request,'cadastrar_recurso') is not True:
        return autenticar_permissao(request,'cadastrar_recurso')
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
            messages.success(request, 'Recurso cadastrado com sucesso!')
            return HttpResponseRedirect(reverse('cadastro-recurso'))
        
    context = {'form': form}
    return render(request, 'recurso/cadastro_recurso.html', context)

# @require_POST

def cadastro_tipo_recurso(request):
    if autenticar_permissao(request,'cadastrar_tipo_recurso') is not True:
        return autenticar_permissao(request,'cadastrar_tipo_recurso')
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
            messages.success(request, 'Tipo de recurso cadastrado com sucesso!')
            return redirect('cadastro-tipo-recurso')
            
    context = {'form':form}
    return render(request, 'recurso/cadastro_tipo_recurso.html', context)

# @require_POST


def reserva_recurso(request):
    if autenticar_permissao(request,'reservar_recurso') is not True:
        return autenticar_permissao(request,'reservar_recurso')
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
    if autenticar_permissao(request,'listar_emprestimos') is not True:
        return autenticar_permissao(request,'listar_emprestimos')
    status = request.GET.get('status')
    usuario = request.GET.get('usuario')
    solicitante = request.GET.get('solicitante')

    emprestimos = Emprestimo.objects.all()

    if status:
        if status == 'ativos':
            emprestimos = emprestimos.filter(horaEntrada__isnull=True)
        elif status == 'devolvidos':
            emprestimos = emprestimos.filter(horaEntrada__isnull=False)

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
    if autenticar_permissao(request,'listar_local') is not True:
        return autenticar_permissao(request,'listar_local')
    locais = Local.objects.all()
    tipo = request.GET.get('tipo')
    bloco = request.GET.get('bloco')
    capacidade = request.GET.get('capacidade')
    sort = request.GET.get('sort', 'nome')

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
        'sort': sort,
    }

    return render(request, 'local/listar_local.html', context)


def verificar_reservas(local):
    """ Verifica se um local está reservado por alguma reserva. """
    return ReservaSemanal.objects.filter(local=local).exists() or ReservaDiaUnico.objects.filter(local=local).exists()

@login_required(login_url='/usuarios/login/')
def editar_local(request, pk):
    local = get_object_or_404(Local, pk=pk)
    
    # Verifica se o local está reservado antes de permitir a edição
    if verificar_reservas(local):
        return HttpResponseForbidden("Não é possível editar este local porque está sendo reservado.")

    if request.method == 'POST':
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            novo_nome = form.cleaned_data.get('nome')

            # Verificar se o nome do local já existe
            if Local.objects.filter(nome=novo_nome).exclude(pk=local.pk).exists():
                context = {'erro': 'Já existe um local com esse nome!', 'form': form, 'local': local}
                return render(request, 'local/editar_local.html', context)

            form.save()
            return redirect('listar_local')
    else:
        form = LocalForm(instance=local)

    context = {
        'form': form,
        'local': local,
    }
    return render(request, 'local/editar_local.html', context)

@login_required(login_url='/usuarios/login/')
def remover_local(request, pk):
    local = get_object_or_404(Local, pk=pk)
    
    # Verifica se o local pode ser removido
    if verificar_reservas(local):
        return HttpResponseForbidden("Não é possível remover este local porque está sendo reservado.")

    local.delete()
    return redirect('listar_local')

# @require_GET

def listar_recursos(request):
    if autenticar_permissao(request,'listar_recursos') is not True:
        return autenticar_permissao(request,'listar_recursos')
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
    if autenticar_permissao(request,'cadastro_reserva_semanal') is not True:
        return autenticar_permissao(request,'cadastro_reserva_semanal')
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
    if autenticar_permissao(request,'cadastro_reserva_dia') is not True:
        return autenticar_permissao(request,'cadastro_reserva_dia')
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
    
# @require_http_methods(['DELETE'])    
def delete_reserva_semanal(request, id):
    reserva = ReservaSemanal.objects.get(pk=id)
    reserva.delete()
    return HttpResponseRedirect(reverse('listar-reservas'))
      
# @require_http_methods(['DELETE'])    
def delete_reserva_dia(request, id):
    reserva = ReservaDiaUnico.objects.get(pk=id)
    reserva.delete()
    return HttpResponseRedirect(reverse('listar-reservas'))

def editar_reserva_semanal(request, id):
    reserva = ReservaSemanal.objects.get(pk=id)
    
    if request.method == 'POST':  
        req = request.POST
        horarios_vetor = converter_horarios(req.getlist('dias'), req.getlist('horarios'))
        horarios = Horario.objects.filter(id__in=horarios_vetor)
        reserva.horarios.set(horarios)
        reserva.matSolicitante = Usuario.objects.get(matricula=req.get('matSolicitante'))
        reserva.save()
        
        messages.success(request, 'Reserva editada com sucesso!')
        return redirect('listar-reservas')
    else:
        form = ReservaForm()
        horarios_dias = converter_horarios_back(map(lambda horario: horario['id'], reserva.horarios.values()));
        reserva.horarios_form = mark_safe(json.dumps(horarios_dias['horarios']))
        reserva.dias = mark_safe(json.dumps(horarios_dias['dias']))
        
        context = {
            'form': form,
            'reserva': reserva
        }
        return render(request, 'reserva/editarReservaSemanal.html', context=context)

def editar_reserva_dia(request, id):
    reserva = ReservaDiaUnico.objects.get(pk=id)
    
    if request.method == 'POST':  
        reserva.diaHoraInicio = datetime.strptime(request.POST.get('diaHoraInicio'),'%Y-%m-%dT%H:%M')
        reserva.diaHoraFim = datetime.strptime(request.POST.get('diaHoraFim'),'%Y-%m-%dT%H:%M')
        reserva.matSolicitante = Usuario.objects.get(matricula=request.POST.get('matSolicitante'))
        reserva.save()
        
        messages.success(request, 'Reserva editada com sucesso!')
        return redirect('listar-reservas')
    else:
        form = ReservaDiaForm()
        reserva.diaHoraInicio = reserva.diaHoraInicio.strftime('%Y-%m-%dT%H:%M')
        reserva.diaHoraFim = reserva.diaHoraFim.strftime('%Y-%m-%dT%H:%M')
        
        context = {
            'form': form,
            'reserva': reserva
        }
        return render(request, 'reserva/editarReservaDia.html', context=context)

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
        capacidade__gte=pessoas,
        bloco=bloco
    )
    print(locais_final)
    context = {'locais':locais_final}
    return render(request, 'reserva/local_option.html', context)

# @require_POST
def efetuar_chamado(request):
    if autenticar_permissao(request,'efetuar_chamados') is not True:
        return autenticar_permissao(request,'efetuar_chamados')
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
    if autenticar_permissao(request,'listar_reservas') is not True:
        return autenticar_permissao(request,'listar_reservas')
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

def recurso_delete(request, id):
    recurso = Recurso.objects.get(pk=id)
    recurso.delete()
    messages.success(request, 'Recurso excluído com sucesso!')
    return redirect('listar-recurso')

def recurso_edit(request, id):
    recurso = Recurso.objects.get(pk=id)
    if request.method == 'POST':
        form = RecursoForm(request.POST, instance=recurso)
        form.disable_fields_except_funcionando()
        if form.is_valid():
            Recurso.objects.filter(pk=id).update(funcionando=form.cleaned_data['funcionando'])
            messages.success(request, 'Recurso editado com sucesso!')
            return redirect('listar-recurso')
    else:
        form = RecursoForm(instance=recurso)
        form.disable_fields_except_funcionando()
    return render(request, 'recurso/editar_recurso.html', {'form': form})

def autenticar_permissao(request, permissao):
    if request.user.is_authenticated is not True:
        return HttpResponse("Você precisa estar logado para acessar esta página.")
    if has_permission(request.user, permissao) is not True:
        return HttpResponse("Seu usuário não tem permissão de acessar essa página")
    return True