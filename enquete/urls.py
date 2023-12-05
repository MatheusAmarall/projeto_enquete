from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('user-logout/', views.user_logout, name='user-logout'),
    path('criacao-enquete/', views.create, name='criacao-enquete'),
    path('votacao/<int:id>', views.vote, name='votacao'),
    path('resultado/<int:id>', views.result, name='resultado'),
]