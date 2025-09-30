from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='index.html'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('atualizar/', views.atualizar_produto, name='atualizar_produto'),

]