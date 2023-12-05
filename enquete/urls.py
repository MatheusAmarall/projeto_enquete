from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('user-logout/', views.user_logout, name='user-logout'),
    path('criacao-enquete/', views.create, name='criacao-enquete'),
    path('votacao/<int:id>', views.vote, name='votacao'),
    path('resultado/<int:id>', views.result, name='resultado'),
    path('enquetes-votadas/', views.polls_voted, name='enquetes-votadas'),
    path('fechar-enquete/<int:id>', views.close_poll, name='fechar-enquete')
]