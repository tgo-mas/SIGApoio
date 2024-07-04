from django.shortcuts import render 
# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')  

def cad_page(request):
    return render(request, 'usuarios/cad_page.html')