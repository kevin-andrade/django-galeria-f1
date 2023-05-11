from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import auth, messages

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms


def index(request):
    fotografias = Fotografia.objects.all()

    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.all()

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})

def nova_imagem(request):
    form = FotografiaForms

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Fotografia cadastrada com sucesso!")
            return redirect('index')

    return render(request, 'galeria/nova-imagem.html', {"form": form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(pk=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)

        if form.is_valid():
            form.save()
            messages.success(request, "Fotografia editada com sucesso!")
            return redirect("imagem")

    return render(request, 'galeria/editar-imagem.html', {"form": form, "foto_id": foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, "Fotografia deletada com sucesso!")

    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"cards": fotografias})