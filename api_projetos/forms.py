from django import forms
from .models import Projeto
from api_usuarios.models import Usuario

class ProjetoForm(forms.ModelForm):
    participantes = forms.ModelMultipleChoiceField(
        queryset=Usuario.objects.filter(tipo='estudante'),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Estudantes Participantes"
    )

    # Adicionando campos de data
    data_inicio = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data de Início"
    )
    data_fim = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data de Fim"
    )

    class Meta:
        model = Projeto
        fields = [
            'titulo', 
            'cliente', 
            'status', 
            'professor_responsavel', 
            'participantes',
            'data_inicio',   # adicionado
            'data_fim'       # adicionado
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['professor_responsavel'].queryset = Usuario.objects.filter(tipo='professor')
