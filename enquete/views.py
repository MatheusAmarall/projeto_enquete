from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Enquetes

def index(request):
    return render(request, 'pages/index.html')

def user_logout(request):
    auth.logout(request)
    return redirect('home')

def create(request):
    if request.method == 'POST':
        new_question = request.POST.get('new_question')
        opcao_um = request.POST.get('opcao1')
        opcao_dois = request.POST.get('opcao2')
        opcao_tres = request.POST.get('opcao3')
        opcao_quatro = request.POST.get('opcao4')

        Enquetes.objects.create(
            pergunta=new_question,
            opcao_um=opcao_um,
            opcao_dois=opcao_dois,
            opcao_tres=opcao_tres,
            opcao_quatro=opcao_quatro
        )

        return redirect('home')
    else:
        return render(request, 'pages/criacao_enquete.html')
