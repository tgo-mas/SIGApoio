from .models import Recurso, TipoRecurso
from django.shortcuts import render 
from .forms import RecursoForm, ChamadoForm, TipoRecursoForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LocalForm, RecursoForm
from django.views.decorators.http import require_POST, require_GET, require_safe, require_http_methods

@require_GET
def home(request):
    return render(request,'index.html')  

@require_POST
def cad_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page') 
    else:
        form = LocalForm()
    return render(request, 'usuarios/cad_page.html', {'form': form})

@require_GET
def success_page(request):
    return render(request, 'usuarios/success_page.html')

@require_POST
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

@require_POST
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

@require_POST
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
            return HttpResponseRedirect(reverse('cadastro-tipo-recurso'))
            
    context = {'form':form}
    return render(request, 'recurso/cadastro_tipo_recurso.html', context)
