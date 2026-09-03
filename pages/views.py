from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Mensagens


def index(request: HttpRequest) -> HttpResponse:

    mural_recados = Mensagens.objects.order_by('-id')[:9]

    contexto = {
        'titulo_pagina': 'Mural_De_Recados',
        'descricao': 'Compartilhar recados de usuarios',
        'mural_recados': mural_recados,
    }

    return render(request, 'pages/index.html', contexto)


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