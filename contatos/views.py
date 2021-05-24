from django.shortcuts import render
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def detalhes(request, id_contato):
    contato = Contato.objects.get(id=id_contato)
    return render(request, 'contatos/detalhes.html', {
        'contato': contato
    })
