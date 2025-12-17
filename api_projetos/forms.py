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
            'data_inicio',
            'data_fim'  
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['professor_responsavel'].queryset = Usuario.objects.filter(tipo='professor')

    def save(self, commit=True):
        instance = super().save(commit=False)
    
        instance.data_fim_prevista = self.cleaned_data['data_fim']
        if commit:
            instance.save()
            
            if self.cleaned_data.get('participantes'):
                if instance.equipe:
                    instance.equipe.membros.set(self.cleaned_data['participantes'])
        return instance
