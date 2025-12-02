from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    
    projetos = []  
    usuarios = []
    context = {
        'projetos': projetos,
        'usuarios': usuarios,
    }
    return render(request, 'home.html', context)



def sair(request):
    logout(request)
    return redirect('login')
