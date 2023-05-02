from django.db import models


class Fotografia(models.Model):

    nome = models.CharField(max_length=130, blank=False, null=False)
    legenda = models.CharField(max_length=130, blank=False, null=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.nome
    