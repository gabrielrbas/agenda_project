from django.forms.forms import Form
from django.shortcuts import redirect, render, get_object_or_404
from .models import Contato, FormContato


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


def novo_contato(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'contatos/novo_contato.html', {
            'form': form
        })

    form = FormContato(request.POST, request.FILES)
    if not form.is_valid():
        form = FormContato(request.POST)
        return render(request, 'contatos/novo_contato.html', {
            'form': form
        })

    form.save()
    return redirect('index')
