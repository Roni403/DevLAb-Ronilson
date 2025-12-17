from django import forms
from .models import Equipe
from api_usuarios.models import Usuario
from api_projetos.models import Projeto

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome', 'descricao', 'lider', 'projeto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['lider'].queryset = Usuario.objects.filter(tipo='estudante')
        
        self.fields['projeto'].queryset = Projeto.objects.all()

        self.fields['nome'].label = "Nome da Equipe"
        self.fields['descricao'].label = "Descrição"
        self.fields['lider'].label = "Líder da Equipe"
        self.fields['projeto'].label = "Projeto"
