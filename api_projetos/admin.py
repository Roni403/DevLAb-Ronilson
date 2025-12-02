from django.contrib import admin
from .models import Projeto, ParticipacaoProjeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'status', 'data_inicio', 'data_fim_prevista', 'professor_responsavel')
    list_filter = ('status',)
    search_fields = ('titulo', 'cliente')
    
    fields = ('titulo', 'descricao', 'cliente', 'status', 'data_inicio', 'data_fim_prevista', 'professor_responsavel')

@admin.register(ParticipacaoProjeto)
class ParticipacaoProjetoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'projeto', 'papel')
