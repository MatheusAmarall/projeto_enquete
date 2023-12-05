from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Enquetes

def index(request):
    enquetes = Enquetes.objects.all()
    return render(request, 'pages/index.html', {"enquetes":enquetes})

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

def vote(request, id):
    enquete = Enquetes.objects.get(id = id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            enquete.qtd_opcao_um += 1
        elif selected_option == 'option2':
            enquete.qtd_opcao_dois += 1
        elif selected_option == 'option3':
            enquete.qtd_opcao_tres += 1
        elif selected_option == 'option4':
            enquete.qtd_opcao_quatro += 1
        else:
            return HttpResponse(400, 'Invalid form option')
    
        enquete.save()

        return redirect('resultado', enquete.id)

    return render(request, 'resultado.html', {"enquete":enquete})