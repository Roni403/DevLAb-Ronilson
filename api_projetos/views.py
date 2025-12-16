from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projeto, Equipe, ParticipacaoEquipe
from .forms import ProjetoForm
from api_usuarios.forms import CriarEquipeForm
from api_usuarios.models import Usuario


@login_required
def home_coordenador(request):
    if request.user.tipo != 'coordenador':
        return redirect('login')

    projetos = Projeto.objects.all()
    equipes = Equipe.objects.all()

    return render(request, 'home_coordenador.html', {
        'projetos': projetos,
        'equipes': equipes
    })


@login_required
def criar_projeto(request):
    if request.user.tipo != 'coordenador':
        return redirect('login')

    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_coordenador')
    else:
        form = ProjetoForm()

    return render(request, 'criar_projeto.html', {'form': form})


@login_required
def editar_projeto(request, pk):
    if request.user.tipo != 'coordenador':
        return redirect('login')

    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('home_coordenador')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'editar_projeto.html', {'form': form, 'projeto': projeto})


@login_required
def deletar_projeto(request, pk):
    if request.user.tipo != 'coordenador':
        return redirect('login')

    projeto = get_object_or_404(Projeto, pk=pk)
    projeto.delete()
    return redirect('home_coordenador')


@login_required
def detalhe_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    equipes = Equipe.objects.filter(projetos=projeto)
    return render(request, 'detalhe_projeto.html', {'projeto': projeto, 'equipes': equipes})


@login_required
def home_professor(request):
    if request.user.tipo != 'professor':
        return redirect('login')

    projetos = Projeto.objects.filter(professor_responsavel=request.user)
    equipes = Equipe.objects.filter(projetos__in=projetos).distinct()

    return render(request, 'home_professor.html', {
        'projetos': projetos,
        'equipes': equipes
    })


@login_required
def home_estudante(request):
    if request.user.tipo != 'estudante':
        return redirect('login')

    participacoes = ParticipacaoEquipe.objects.filter(usuario=request.user)
    equipes = Equipe.objects.filter(participacaoequipe__in=participacoes).distinct()
    
    
    projetos = Projeto.objects.filter(id__in=equipes.values_list('projetos__id', flat=True)).distinct()

    return render(request, 'home_estudante.html', {
        'projetos': projetos,
        'equipes': equipes
    })
