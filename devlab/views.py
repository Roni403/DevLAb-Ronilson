from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from api_usuarios.models import Usuario
from .models import Projeto
from api_equipes.models import Equipe, ParticipacaoProjeto


@login_required
def home_coordenador(request):
    if request.user.tipo != 'coordenador':
        return redirect('login')
    projetos = Projeto.objects.all()
    equipes = Equipe.objects.all()
    return render(request, 'home_coordenador.html', {'projetos': projetos, 'equipes': equipes})


@login_required
def home_professor(request):
    if request.user.tipo != 'professor':
        return redirect('login')
    projetos = Projeto.objects.filter(professor_responsavel=request.user)
    equipes = Equipe.objects.filter(projeto__in=projetos)
    return render(request, 'home_professor.html', {'projetos': projetos, 'equipes': equipes})


@login_required
def home_estudante(request):
    if request.user.tipo != 'estudante':
        return redirect('login')
    participacoes = ParticipacaoProjeto.objects.filter(usuario=request.user)
    projetos = [p.projeto for p in participacoes]
    equipes = [p.equipe for p in participacoes if hasattr(p, 'equipe')]
    return render(request, 'home_estudante.html', {'projetos': projetos, 'equipes': equipes})


@login_required
def criar_projeto(request):
    if request.user.tipo != 'coordenador':
        return redirect('login')
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        cliente = request.POST['cliente']
        status = request.POST['status']
        data_inicio = request.POST['data_inicio']
        data_fim_prevista = request.POST['data_fim_prevista']
        professor_id = request.POST['professor']
        professor = get_object_or_404(Usuario, id=professor_id)
        Projeto.objects.create(
            titulo=titulo,
            descricao=descricao,
            cliente=cliente,
            status=status,
            data_inicio=data_inicio,
            data_fim_prevista=data_fim_prevista,
            professor_responsavel=professor
        )
        return redirect('home_coordenador')
    professores = Usuario.objects.filter(tipo='professor')
    return render(request, 'criar_projeto.html', {'professores': professores})


@login_required
def detalhe_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    equipes = Equipe.objects.filter(projeto=projeto)
    participacoes = ParticipacaoProjeto.objects.filter(projeto=projeto)
    return render(request, 'detalhe_projeto.html', {'projeto': projeto, 'equipes': equipes, 'participacoes': participacoes})
