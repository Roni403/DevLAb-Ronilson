from django.urls import path
from .views import CriarEquipeView, DeletarEquipeView, ListarEquipesView

urlpatterns = [
    path("criar/", CriarEquipeView.as_view()),
    path("deletar/<int:id_equipe>/", DeletarEquipeView.as_view()),
    path("listar/", ListarEquipesView.as_view()),
]
