from django.db import models


class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("ALPINE", 'Alpine'),
        ("ASTON MARTIN", 'Aston Martin'),
        ("FERRARI", 'Ferrari'),
        ("RED BULL", 'Red Bull'),
        ("MERCEDES", 'Mercedes'),
        ("MCLAREN", 'Mclaren'),
    ]

    nome = models.CharField(max_length=130, blank=False, null=False)
    legenda = models.CharField(max_length=130, blank=False, null=False)
    categoria = models.CharField(max_length=100, null=False, choices=OPCOES_CATEGORIA, default="" )
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.nome
    