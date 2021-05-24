from django.shortcuts import render, get_object_or_404
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def detalhes(request, id_contato):
    contato = get_object_or_404(Contato, id=id_contato)
    return render(request, 'contatos/detalhes.html', {
        'contato': contato
    })
