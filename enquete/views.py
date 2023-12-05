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
        pass
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