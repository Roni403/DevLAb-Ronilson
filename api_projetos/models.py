from django.db import models
from api_usuarios.models import Usuario

class Projeto(models.Model):
    STATUS_CHOICES = (
        ('planejado', 'Planejado'),
        ('em_andamento', 'Em andamento'),
        ('concluido', 'Concluído'),
    )
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    cliente = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planejado')
    data_inicio = models.DateField(null=True, blank=True)
    data_fim_prevista = models.DateField(null=True, blank=True)
    participantes = models.ManyToManyField(Usuario, through='ParticipacaoProjeto', related_name='projetos')

    
    professor_responsavel = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'tipo': 'professor'},
        related_name='projetos_como_professor'
    )

    def __str__(self):
        return self.titulo

class ParticipacaoProjeto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    papel = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.usuario} -> {self.projeto}"
