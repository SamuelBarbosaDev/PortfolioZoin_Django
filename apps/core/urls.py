from django.urls import path
from core.views import *

urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio'),
    path('detalhes/<int:pk>/', PortfolioDetalhesView.as_view(), name='portfolio_detalhes'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contatos/', ContatosView.as_view(), name='contatos'),
]
