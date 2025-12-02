from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('coordenador','Coordenador'),
        ('professor','Professor'),
        ('estudante','Estudante'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO)
    telefone = models.CharField(max_length=20, blank=True)
    curso = models.CharField(max_length=50, blank=True)
    matricula = models.CharField(max_length=20, blank=True)

    
    groups = models.ManyToManyField(
        Group,
        related_name='usuarios_custom',
        blank=True,
        help_text='Grupos aos quais este usuário pertence.',
        verbose_name='grupos',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios_custom_permissions',
        blank=True,
        help_text='Permissões específicas deste usuário.',
        verbose_name='permissões do usuário',
    )

    def __str__(self):
        return f"{self.username} ({self.tipo})"
