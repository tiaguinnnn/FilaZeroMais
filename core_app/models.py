from django.db import models

# Create your models here.
class UnidadeSaude(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    capacidade = models.PositiveIntegerField()
    ocupacao_atual = models.PositiveIntegerField(default=0)

    def semaforo(self):
        percentual = self.ocupacao_atual / self.capacidade
        if percentual < 0.5:
            return "verde"
        elif percentual < 0.8:
            return "amarelo"
        return "vermelho"
