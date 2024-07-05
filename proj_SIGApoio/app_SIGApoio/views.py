from django.shortcuts import render, redirect
from .forms import LocalForm
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

