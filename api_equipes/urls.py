from django.urls import path
from .views import CriarEquipeView, DeletarEquipeView, ListarEquipesView

urlpatterns = [
    path("criar/", CriarEquipeView.as_view(), name="criar_equipe"),
    path("deletar/<int:id_equipe>/", DeletarEquipeView.as_view(), name="deletar_equipe"),
    path("listar/", ListarEquipesView.as_view(), name="listar_equipes"),
]
