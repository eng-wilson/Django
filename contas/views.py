from django.shortcuts import render
from django.http import HttpResponse
from .forms import TransacaoForm
from .models import Transacao
from django.shortcuts import render, redirect
import datetime


def home(request):

    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)

    return render(request, 'contas/home.html', data)
# Create your views here.


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form

    return render(request, 'contas/form.html', {'form': form})


def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['transacao'] = transacao
    data['form'] = form

    return render(request, 'contas/form.html', data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
