from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from django.contrib.auth import logout
from .models import Projeto, ParticipacaoProjeto
from .serializers import ProjetoSerializer, ParticipacaoProjetoSerializer
from api_usuarios.models import Usuario


@login_required(login_url='login')
def home(request):
    """
    Página inicial do sistema.
    Decide qual home renderizar conforme o tipo do usuário.
    """
    user = request.user

    projetos = Projeto.objects.all()
    usuarios = Usuario.objects.all()

    query = request.GET.get('q')
    if query:
        projetos = projetos.filter(titulo__icontains=query)
        usuarios = usuarios.filter(username__icontains=query)

    context = {
        'projetos': projetos,
        'usuarios': usuarios,
    }

    tipo = (user.tipo or '').strip().lower()

    if tipo in ['estudante', 'aluno']:
        return render(request, 'home_estudante.html', context)

    elif tipo in ['professor', 'professora']:
        return render(request, 'home_professor.html', context)

    elif tipo in ['coordenador', 'coordenadora', 'coordenação']:
        return render(request, 'home_coordenador.html', context)

    # Fallback visível (debug)
    return render(
        request,
        'home.html',
        {**context, 'erro_tipo': f'Tipo não reconhecido: "{user.tipo}"'}
    )


def sair(request):
    """
    Faz logout do usuário e redireciona para a página de login.
    """
    logout(request)
    return redirect('login')


class IsCoordenadorOrProfessor(permissions.BasePermission):
    """
    Coordenador: pode fazer tudo.
    Professor: pode criar/deletar projetos e gerenciar alunos.
    Aluno: apenas GET (read-only).
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.tipo == 'coordenador':
                return True
            elif request.user.tipo == 'professor':
                return True
            elif request.user.tipo == 'estudante':
                return request.method in permissions.SAFE_METHODS
        return False


class ProjetoViewSet(viewsets.ModelViewSet):
    """
    API de Projetos
    """
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    permission_classes = [IsCoordenadorOrProfessor]


class ParticipacaoProjetoViewSet(viewsets.ModelViewSet):
    """
    API de Participações em Projetos
    """
    queryset = ParticipacaoProjeto.objects.all()
    serializer_class = ParticipacaoProjetoSerializer
    permission_classes = [IsCoordenadorOrProfessor]


@login_required(login_url='login')
def redirecionar_usuario(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    return redirect('home')


# ================= Funções adicionais para a home =================
@login_required(login_url='login')
def lista_projetos(request):
    projetos = Projeto.objects.all()
    context = {'projetos': projetos}
    return render(request, 'lista_projetos.html', context)


@login_required(login_url='login')
def lista_equipes(request):
    participacoes = ParticipacaoProjeto.objects.all()
    context = {'participacoes': participacoes}
    return render(request, 'lista_equipes.html', context)
