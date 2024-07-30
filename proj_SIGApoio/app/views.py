from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST, require_GET, require_safe, require_http_methods
from .forms import LocalForm, RecursoForm, TipoRecursoForm, ReservaForm, ChamadoForm, ReservaDiaForm, ReservaMensalForm
from .models import TipoRecurso, Recurso, Local, ReservaSemanal, Usuario, Horario, TipoLocal, Emprestimo
from .bo.horarios import converter_horarios
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json

# @require_GET
def home(request):
    return render(request,'index.html')  

#@require_http_methods(['GET','POST'])
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


@require_safe
def success_page(request):
    return render(request, 'local/success_page.html')

# @require_http_methods(['GET','POST'])
# @require_POST
def cadastroRecurso(request):
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

  
#@require_http_methods(['GET','POST'])
# @require_POST
def efetuarChamado(request):
    if request.method != 'POST':
        form = ChamadoForm()
    else:
        form = ChamadoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('efetuar-chamado'))
        
    context = {'form': form}
    return render(request, 'chamado/efetuar_chamado.html', context)


#@require_http_methods(['GET','POST'])
# @require_POST
def cadastroTipoRecurso(request):
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

def reserva_recurso(request):
    tipos_recursos = TipoRecurso.objects.all()
    
    if request.method == 'POST':
        reserva_form = ReservaForm(request.POST)
        if reserva_form.is_valid():
            reserva_form.save()
            return redirect('success_page')  # Ajuste o redirecionamento conforme necessário
    else:
        reserva_form = ReservaForm()

    return render(request, 'recurso/reserva_recurso.html', {'reserva_form': reserva_form, 'tipos_recursos': tipos_recursos})


def listar_emprestimos(request):
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

def listarRecursos(request):
    recursos = Recurso.objects.all()
    recursosDisponiveis = Recurso.objects.filter(status=True)
    recursosIndisponiveis = Recurso.objects.filter(status=False)
    recursosFunciona = Recurso.objects.filter(funcionando=True)
    recursosNaoFunciona = Recurso.objects.filter(funcionando=False)
    tipos = TipoRecurso.objects.all()
    context = {'recursos':recursos, 'tipos':tipos, 'recursosDisponiveis':recursosDisponiveis, 'recursosIndisponiveis':recursosIndisponiveis, 'recursosNaoFunciona':recursosNaoFunciona, 'recursosFunciona':recursosFunciona}
    return render(request, 'recurso/listar_recurso.html', context)

def tipoReserva(request):
    return render(request, 'reserva/tipoReserva.html')

def cadastroReservaSemanal(request):
    if request.method != 'POST':
        form = ReservaForm()
        context = {'form': form}
        return render(request, 'reserva/cadastroReserva.html', context)
    else:
        req = request.POST
        form = ReservaForm()
        context = {'form': form, 'message': 'Reserva cadastrada com sucesso!'}
        try:
            resp = Usuario.objects.get(matricula=req['matSolicitante']) # Enquanto a auth não está pronta
            # resp = get_auth_user().get("matricula")                  // Vai ser algo assim depois da autenticação
            solic = Usuario.objects.get(matricula=req['matSolicitante'])
            local = Local.objects.get(id=req['local'])
            horarios_vetor = converter_horarios(req.getlist('dias'), req.getlist('horarios')) # Junta os dias e horarios
            horarios = Horario.objects.filter(id__in=horarios_vetor)
            novaReserva = ReservaSemanal.objects.create(local=local, matResponsavel=resp, matSolicitante=solic)
            novaReserva.horarios.set(horarios)
            novaReserva.save()
            return render(request, 'reserva/cadastroReserva.html', context)
        except:
            context = {'form': form, 'message': 'Erro no cadastro da reserva', 'error': True}
            return render(request, 'reserva/cadastroReserva.html', context)
    
def cadastroReservaDia(request):
    form = ReservaDiaForm()
    context = {'form': form }
    return render(request, 'reserva/cadastroReservaDia.html', context)

def cadastroReservaMensal(request):
    form = ReservaMensalForm()
    context = {'form': form}
    return render(request, 'reserva/cadastroReservaMensal.html', context)

@csrf_exempt
def getLocais(request):
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