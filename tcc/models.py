from django.db import models
from django.contrib.postgres.fields import ArrayField

class Autor(models.Model):

    ft_nome = models.CharField(max_length=200)
    ult_nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.ft_nome


class Orientador(models.Model):

    ft_nome = models.CharField(max_length=200)
    ult_nome = models.CharField(max_length=200)
    link_curriculo = models.URLField(max_length=200)

    def __str__(self):
        return self.ft_nome

class Curso(models.Model):

    nome = models.CharField(max_length=200)
    modalidade = [
        ('B', 'bacharelado'),
        ('L', 'licenciatura'),
        ('T', 'tecnologico'),
    ]

    def __str__(self):
        return self.nome

class TCC(models.Model):

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    orientador = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)
    ano_doc = models.DateField(verbose_name='Ano documento')
    arquivo_doc = models.FileField(upload_to='docs')
    palavras_chave = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.titulo