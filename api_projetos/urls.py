from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjetoViewSet,
    ParticipacaoProjetoViewSet,
    lista_projetos,
    lista_equipes,
    home_coordenador,
    criar_projeto,
    editar_projeto,
    deletar_projeto,
    detalhe_projeto,
    home_professor,
    home_estudante,
    adicionar_aluno_projeto,
    remover_aluno_projeto   
)

router = DefaultRouter()
router.register(r'projetos', ProjetoViewSet)
router.register(r'participacoes', ParticipacaoProjetoViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('home/coordenador/', home_coordenador, name='home_coordenador'),
    path('home/professor/', home_professor, name='home_professor'),
    path('home/estudante/', home_estudante, name='home_estudante'),

    path('projetos/criar/', criar_projeto, name='criar_projeto'),
    path('projetos/<int:pk>/editar/', editar_projeto, name='editar_projeto'),
    path('projetos/<int:pk>/deletar/', deletar_projeto, name='deletar_projeto'),
    path('projetos/<int:pk>/', detalhe_projeto, name='detalhe_projeto'),

    path(
        'projetos/<int:pk>/adicionar-aluno/',
        adicionar_aluno_projeto,
        name='adicionar_aluno_projeto'
    ),

    path(
        'projetos/remover-aluno/<int:participacao_id>/',
        remover_aluno_projeto,
        name='remover_aluno_projeto'
    ),

    path('lista/', lista_projetos, name='lista_projetos'),
    path('equipes/', lista_equipes, name='lista_equipes'),
]
