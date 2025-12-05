from  django.db import models
from .models import usuario, projeto

# Create your models here.
class Equipe(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='equipes'
    )

    lider = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'tipo': 'Estudante'},
        related_name='equipes_lideradas'
    )

    def __str__(self):
        return self.nome
    
