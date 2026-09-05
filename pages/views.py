from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .models import Mensagens


def index(request: HttpRequest) -> HttpResponse:

    mural_recados = Mensagens.objects.order_by('-id')[:3]

    contexto = {
        'titulo_pagina': 'Mural_De_Recados',
        'descricao': 'Compartilhar recados de usuarios',
        'mural_recados': mural_recados,
    }

    return render(request, 'pages/index.html', contexto)

@login_required
def mensagens(request: HttpRequest) -> HttpResponse:

    contexto = {}

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        data = request.POST.get('data', '').strip()
        mensagem = request.POST.get('mensagem', '').strip()

        Mensagens.objects.create(
            nome=nome,
            data=data,
            mensagem=mensagem,
        )

        contexto = {
            'mensagem_enviada': True,
            'mensagem': mensagem,
        }

    return render(request, 'pages/mensagens.html', contexto)

def cadastro_view(request: HttpRequest) -> HttpResponse:
    contexto = {}

    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        sobrenome = request.POST.get("sobrenome", "").strip()
        email = request.POST.get("email", "").strip()
        senha = request.POST.get("senha", "").strip()
        confirmar_senha = request.POST.get("confirmar_senha", "").strip()

        if senha != confirmar_senha:
            contexto["erro"] = "As senhas informadas não coincidem."
            return render(request, "pages/cadastro.html", contexto)

        if User.objects.filter(username=email).exists():
            contexto["erro"] = "Já existe uma conta cadastrada com este e-mail."
            return render(request, "pages/cadastro.html", contexto)

        User.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome,
            last_name=sobrenome,
        )

        messages.success(request=request, message="Cadastro realizado com sucesso.")
        return redirect("pages:login")  

    return render(request, "pages/cadastro.html", contexto)


def login_view(request: HttpRequest) -> HttpResponse:
    contexto = {}

    next_url = request.GET.get("next", "")

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        senha = request.POST.get("senha", "")

        usuario = authenticate(request=request, username=email, password=senha)

        if usuario is not None:
            login(request=request, user=usuario)

            messages.success(request=request, message="Login realizado com sucesso.") 

            if next_url:
                return redirect(next_url)

            return redirect("pages:index")
        else:
            contexto["erro"] = "E-mail ou senha inválidos."

    return render(request, "pages/login.html", contexto)


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request=request)

    messages.info(request=request, message="Você saiu da sua conta.")

    return redirect("pages:index")


def lista(request: HttpRequest) -> HttpResponse:
    mural_recados = Mensagens.objects.order_by('-id')

    contexto = {
        "mensagens": mural_recados,
    }

    return render(
        request,
        "pages/lista.html",
        contexto,
    )


@login_required
def meus_recados(request: HttpRequest) -> HttpResponse:

    recados = Mensagens.objects.all().order_by("-id")

    contexto = {"recados": recados}

    return render(
        request=request, template_name="pages/meus_recados.html", context=contexto
    )