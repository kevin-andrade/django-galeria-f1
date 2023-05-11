from django.db import models
from django.contrib.auth.models import User


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
    publicada = models.BooleanField(default=True)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name= 'user'
    )

    def __str__(self):
        return self.nome
    