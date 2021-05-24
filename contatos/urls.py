from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_contato>', views.detalhes, name='detalhes'),
    path('novo_contato/', views.novo_contato, name='novo_contato'),
]
