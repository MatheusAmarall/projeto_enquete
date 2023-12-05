from django.shortcuts import render, redirect
from django.contrib import auth

def index(request):
    return render(request, 'pages/index.html')

def user_logout(request):
    auth.logout(request)
    return redirect('home')

def create(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'pages/criacao_enquete.html')