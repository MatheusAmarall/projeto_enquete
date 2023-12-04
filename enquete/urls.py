from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('user-logout/', views.user_logout, name='user-logout')
]