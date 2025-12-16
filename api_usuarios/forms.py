from django import forms
from .models import Usuario
from api_projetos.models import Equipe


class EditarPerfilForm(forms.ModelForm):
    senha_nova = forms.CharField(
        label='Nova Senha',
        widget=forms.PasswordInput,
        required=False,
        help_text='Deixe em branco se não quiser alterar a senha.'
    )

    class Meta:
        model = Usuario
        fields = ['email', 'matricula']  

    def save(self, commit=True):
        usuario = super().save(commit=False)
        senha = self.cleaned_data.get('senha_nova')
        if senha:
            usuario.set_password(senha)
        if commit:
            usuario.save()
        return usuario


class EditarUsuarioForm(forms.ModelForm):
    senha_nova = forms.CharField(
        label='Nova Senha',
        widget=forms.PasswordInput,
        required=False,
        help_text='Deixe em branco se não quiser alterar a senha.'
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'tipo', 'matricula']  

    def save(self, commit=True):
        usuario = super().save(commit=False)
        senha = self.cleaned_data.get('senha_nova')
        if senha:
            usuario.set_password(senha)
        if commit:
            usuario.save()
        return usuario


class CriarEquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome', 'descricao', 'membros']


class CriarUsuarioForm(forms.ModelForm):
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput
    )
    confirmar_senha = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'tipo', 'matricula']  

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar = cleaned_data.get('confirmar_senha')
        if senha and senha != confirmar:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['senha'])
        if commit:
            usuario.save()
        return usuario
