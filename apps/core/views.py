from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from core.models import *
# Create your views here.

class PortfolioView(ListView):
    model = Portfolio
    template_name = 'core/portfolio.html'
    context_object_name = 'portfolio'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        contato_model = Contato.objects.all().order_by('-data_de_criação').first()
        context.update({
            'sobre': Sobre.objects.all().order_by('-data_de_criação').first(),
            'contatos': contato_model,
            'redes_sociais': ContatoRedeSocial.objects.filter(add_redeSocial=contato_model),
        })
        return context

    def get_queryset(self):
        return Portfolio.objects.all().order_by('-data_de_criação')


class PortfolioDetalhesView(UpdateView):
    model = Portfolio
    fields = ['titulo', 'descrição']
    template_name = 'core/portfolio_detalhes.html'
    context_object_name = 'detalhes'


class SobreView(ListView):
    model = Sobre
    template_name = 'core/sobre.html'
    context_object_name = 'sobre'

    def get_context_data(self, **kwargs):
        context = super(SobreView, self).get_context_data(**kwargs)
        contato_model = Contato.objects.all().order_by('-data_de_criação').first()
        context.update({
            'depoimentos': Portfolio.objects.all().order_by('-data_de_criação'),
            'contatos': contato_model,
            'redes_sociais': ContatoRedeSocial.objects.filter(add_redeSocial=contato_model),
        })
        return context

    def get_queryset(self):
        return Sobre.objects.all().order_by('-data_de_criação').first()


class ServicesView(ListView):
    model = Servico
    template_name = 'core/services.html'
    context_object_name = 'servicos'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        contato_model = Contato.objects.all().order_by('-data_de_criação').first()
        context.update({
            'depoimentos': Portfolio.objects.all().order_by('-data_de_criação'),
            'contatos': contato_model,
            'redes_sociais': ContatoRedeSocial.objects.filter(add_redeSocial=contato_model),
            'sobre': Sobre.objects.all().order_by('-data_de_criação').first(),
        })
        return context


class ContatosView(CreateView):
    model = FormularioDeContato
    fields = ['nome', 'email', 'titulo', 'mensagem']
    template_name = 'core/contatos.html'
    success_url = reverse_lazy('portfolio')

    def get_context_data(self, **kwargs):
        context = super(ContatosView, self).get_context_data(**kwargs)
        contato_model = Contato.objects.all().order_by('-data_de_criação').first()
        context.update({
            'contatos': contato_model,
            'redes_sociais': ContatoRedeSocial.objects.filter(add_redeSocial=contato_model),
            'sobre': Sobre.objects.all().order_by('-data_de_criação').first(),
        })
        return context
