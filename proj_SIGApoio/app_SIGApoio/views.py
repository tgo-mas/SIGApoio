from django.shortcuts import render, redirect
from .forms import LocalForm, EmprestimoForm, ReservaForm
# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')  

def cad_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page') 
    else:
        form = LocalForm()
    return render(request, 'usuarios/cad_page.html', {'form': form})

def success_page(request):
    return render(request, 'usuarios/success_page.html')

def res_recurso_view(request):
    if request.method == 'POST':
        if 'confirmar_emprestimo' in request.POST:
            emprestimo_form = EmprestimoForm(request.POST)
            if emprestimo_form.is_valid():
                emprestimo_form.save()
                return redirect('res_recurso')
        elif 'confirmar_reserva' in request.POST:
            reserva_form = ReservaForm(request.POST)
            if reserva_form.is_valid():
                reserva_form.save()
                return redirect('res_recurso')
    else:
        emprestimo_form = EmprestimoForm()
        reserva_form = ReservaForm()

    return render(request, 'usuarios/res_recurso.html', {
        'emprestimo_form': emprestimo_form,
        'reserva_form': reserva_form,
    })