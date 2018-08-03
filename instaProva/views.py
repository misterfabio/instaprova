from django.http import HttpResponse
from django.shortcuts import render


def instaprova(request):
        context = {'nm': ' '}
        if request.method == 'POST':
            nome = request.POST['nome']
            context = {'nm': 'Olá ' + nome}
        return render(request, 'index.html', context)