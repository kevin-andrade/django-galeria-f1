from django.shortcuts import render
from apps.galeria.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.all()

    return render(request, 'galeria/index.html', {'fotografia': fotografias})

def imagem(request):
    return render(request, 'galeria/imagem.html')