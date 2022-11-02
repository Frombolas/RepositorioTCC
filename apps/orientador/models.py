from django.db import models

class Orientador(models.Model):
    Primeiro_nome = models.CharField(max_length=150)
    Ultimo_nome = models.CharField(max_length=150)
    link_curriculo = models.URLField()

    def __str__(self):
        return self.Primeiro_nome + " " + self.Ultimo_nome