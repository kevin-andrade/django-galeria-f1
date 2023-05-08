from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages 

from apps.usuarios.forms import LoginForms, CadastroForms


def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form["email"].value()
            senha = form["senha_1"].value()
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já cadastrado")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')
                
    return render(request, 'usuarios/cadastro.html', {"form": form})