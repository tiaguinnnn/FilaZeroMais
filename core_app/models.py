from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator # Importante para a trava

class UnidadeSaude(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Unidade")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    
    pacientes_em_espera = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)], 
        verbose_name="Pacientes em Espera"
    )
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Unidade de Saúde"
        verbose_name_plural = "Unidades de Saúde"

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    unidade_favorita = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome
