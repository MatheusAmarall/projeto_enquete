from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Enquetes, VotacoesEnquetes
from .utils import send_email
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    todas_enquetes = Enquetes.objects.order_by('-id')
    enquetes = []

    for enquete in todas_enquetes:
        if(enquete.user.id != request.user.id):
            enquetes.append(enquete)

    return render(request, 'pages/index.html', {"enquetes":enquetes})

@login_required
def my_polls(request):
    enquetes = Enquetes.objects.filter(user_id=request.user.id)

    return render(request, 'pages/my_polls.html', {"enquetes":enquetes})

def user_logout(request):
    auth.logout(request)
    return redirect('home')

@login_required
def create(request):
    if request.method == 'POST':
        pergunta = request.POST.get('pergunta')
        opcao_um = request.POST.get('opcao1')
        opcao_dois = request.POST.get('opcao2')
        opcao_tres = request.POST.get('opcao3')
        opcao_quatro = request.POST.get('opcao4')

        Enquetes.objects.create(
            pergunta=pergunta,
            opcao_um=opcao_um,
            opcao_dois=opcao_dois,
            opcao_tres=opcao_tres,
            opcao_quatro=opcao_quatro,
            user_id=request.user.id
        )

        return redirect('minhas-enquetes')
    else:
        return render(request, 'pages/criacao_enquete.html')

@login_required
def result(request, id):
    enquete = Enquetes.objects.get(id=id)
    return render(request, 'pages/resultado.html', {"enquete":enquete})

@login_required
def vote(request, id):
    enquete = Enquetes.objects.get(id=id)

    if request.method == 'POST':
        enquetesVotadas = VotacoesEnquetes.objects.filter(user_id=request.user.id, enquete_id=id)

        if len(enquetesVotadas) > 0:
            messages.warning(request, 'Você já votou nessa enquete.')

            return redirect(reverse('votacao', args=[enquete.id]))
        
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            enquete.qtd_opcao_um += 1
        elif selected_option == 'option2':
            enquete.qtd_opcao_dois += 1
        elif selected_option == 'option3':
            enquete.qtd_opcao_tres += 1
        elif selected_option == 'option4':
            enquete.qtd_opcao_quatro += 1

        VotacoesEnquetes.objects.create(
            user_id=request.user.id,
            enquete_id=id
        )
    
        enquete.save()

        return redirect('resultado', enquete.id)

    return render(request, 'pages/votacao.html', {"enquete":enquete})

@login_required
def polls_voted(request):
    enquetesVotadas = VotacoesEnquetes.objects.filter(user_id=request.user.id)
    enquetes = []
    for enqueteVotada in enquetesVotadas:
        enquetes.append(enqueteVotada.enquete)
    return render(request, 'pages/polls_voted.html', {"enquetes":enquetes})

@login_required
def close_poll(request, id):
    enquete = Enquetes.objects.get(id=id)
    enquete.enquete_aberta = False
    enquete.save()

    votacoes_enquete = VotacoesEnquetes.objects.filter(enquete_id=id)
    # for votacao_enquete in votacoes_enquete:
    #     send_email(f"Resultado enquete: {votacao_enquete.enquete.pergunta}",
    #                 f"""<ul>
    #                         <li>{ enquete.opcao_um } &mdash; <strong>{ enquete.qtd_opcao_um }</strong></li>
    #                         <li>{ enquete.opcao_dois } &mdash; <strong>{ enquete.qtd_opcao_dois }</strong></li>
    #                         <li>{ enquete.opcao_tres } &mdash; <strong>{ enquete.qtd_opcao_tres }</strong></li>
    #                         <li>{ enquete.opcao_quatro } &mdash; <strong>{ enquete.qtd_opcao_quatro }</strong></li>
    #                     </ul>""", 
    #                 votacao_enquete.user.email)

    return redirect('minhas-enquetes')