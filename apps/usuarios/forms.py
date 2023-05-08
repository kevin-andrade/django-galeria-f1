from django import forms
from django.shortcuts import redirect
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label= 'Login',
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite nome de usuário",
            }
        )
    )

    senha = forms.CharField(
        label= "Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de usuário',
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Ex.: kevinandrade'
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=130,
        widget= forms.EmailInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Digite seu email',
            }
        )
    )

    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Digite sua senha',
            }
        )
    )

    senha_2 = forms.CharField(
        label='Confirmação de senha',
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
            "class": 'form-control',
            "placeholder": 'Digite sua senha novamente',
        }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Epaços não são permitidos nesse campo")
            else:
                return nome
            
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email já cadastrado")
            else:
                return email
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas não são iguais")
            else:
                return senha_2