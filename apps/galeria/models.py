from django.db import models


class Fotografia(models.Model):

    nome = models.CharField(max_length=130, blank=False, null=False)
    legenda = models.CharField(max_length=130, blank=False, null=False)
    descricao = models.TextField(null=False, blank=False)
    