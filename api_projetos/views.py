from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .models import Projeto, ParticipacaoProjeto
from .serializers import ProjetoSerializer, ParticipacaoProjetoSerializer
from api_usuarios.models import Usuario

# ---------------- Home ----------------
@login_required
def home(request):
    """
    Página inicial do sistema, mostra projetos e usuários.
    """
    projetos = Projeto.objects.all()
    usuarios = Usuario.objects.all()

    # Busca simples
    query = request.GET.get('q')
    if query:
        projetos = projetos.filter(titulo__icontains=query)
        usuarios = usuarios.filter(username__icontains=query)

    context = {
        'projetos': projetos,
        'usuarios': usuarios
    }
    return render(request, 'home.html', context)

# ---------------- Permissão Customizada ----------------
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
                if request.method in permissions.SAFE_METHODS:
                    return True
                return True
            elif request.user.tipo == 'estudante':
                return request.method in permissions.SAFE_METHODS
        return False

# ---------------- ViewSets da API ----------------
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

# ---------------- Redirecionamento pós-login ----------------
@login_required
def redirecionar_usuario(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    return redirect('home')
