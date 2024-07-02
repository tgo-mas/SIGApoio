from django.shortcuts import render 
from .forms import RecursoForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request,'index.html')  

def cadastroRecurso(request):
    if request.method != 'POST':
        form = RecursoForm()
    else:
        form = RecursoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cadastro-recurso'))
        
    context = {'form': form}
    return render(request, 'recurso/cadastro_recurso.html', context)