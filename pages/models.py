from django.db import models


class Mensagens(models.Model):
    nome = models.CharField(max_length=200)
    data = models.CharField(max_length=150)
    mensagem = models.TextField()

    def __str__(self) -> str:
        return self.mensagem