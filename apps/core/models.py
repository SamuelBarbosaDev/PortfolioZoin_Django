import os
import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.core.exceptions import ValidationError


REDES_SOCIAIS = (
    ('twitter', 'twitter'),
    ('instagram', 'instagram'),
    ('whatsapp', 'whatsapp'),
    ('telegram', 'telegram'),
    ('behance', 'behance'),
    ('twitch', 'twitch'),
    ('github', 'github'),
    ('linkedin', 'linkedin'),
    ('reddit', 'reddit'),
    ('diagram-2-fill', 'diagram-2-fill'),
)


# ==================== PORTFOLIO ====================
class PortfolioCategoria(models.Model):
    categoria = models.CharField(
        max_length=100,
        default='categoria',
    )

    def __str__(self) -> str:
        return self.categoria


class Portfolio(models.Model):
    titulo = models.CharField(
        max_length=50,
        default='titulo',
    )

    categoria = models.ForeignKey(
        PortfolioCategoria,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    frase = models.CharField(
        max_length=100,
        default=' ',
    )

    nome_do_cliente = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    update_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
    )

    url_do_projeto = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    descrição = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
    )

    depoimento_do_cliente = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
    )
    imagem_do_cliente = models.FileField(
        default='default/images/depoimentos_imagem.png',
        upload_to='portfolio/images/',
    )
    capa_do_projeto = models.FileField(
        upload_to='portfolio/images/',
        default='default/images/Em-Breve.jpg',
    )
    data_de_criação = models.DateTimeField(
        'Data de criação',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    @admin.display(
        boolean=True,
        ordering='data_de_criação',
        description='Data de criação',
    )
    def foi_publicado_recentemente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data_de_criação <= now

    def has_image(self, image):
        # print('-'*100, '\n has_image funcionou')

        return (image != None) and (image != '') and (image !=
                                                      'default/images/depoimentos_imagem.png') and (image !=
                                                                                                    'default/images/Em-Breve.jpg')

    def delete(self):
        if self.has_image(self.imagem_do_cliente):
            if os.path.isfile(self.imagem_do_cliente.path):
                os.remove(self.imagem_do_cliente.path)

        if self.has_image(self.capa_do_projeto):
            if os.path.isfile(self.capa_do_projeto.path):
                os.remove(self.capa_do_projeto.path)

        super().delete()
        print('-'*100, '\n delete funcionou')

    def __str__(self):
        return self.titulo


class PortfolioImagem(models.Model):
    add_imagem = models.ForeignKey(
        Portfolio,
        default=None,
        on_delete=models.CASCADE,
    )
    images = models.FileField(
        upload_to='portfolio/images/',
        blank=True,
        null=True,
    )

    def has_image(self):
        print('-'*100, '\n has_image 2', f"{self.images}")
        return self.images != None and self.images != ''

    def remove_image(self):
        if self.has_image():
            if os.path.isfile(self.images.path):
                os.remove(self.images.path)

        self.images = None

    def delete(self):
        self.remove_image()
        super().delete()
        print('-'*100, '\n delete funcionou 2')

    def __str__(self):
        return self.add_imagem.titulo


# ==================== Contato ====================
class Contato(models.Model):
    email = models.EmailField(
        blank=True,
        null=True,
    )

    telefone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
    )

    data_de_criação = models.DateTimeField(
        'Data de criação',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    def __str__(self):
        return self.email


class ContatoRedeSocial(models.Model):
    add_redeSocial = models.ForeignKey(
        Contato,
        default=None,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    rede_social = models.CharField(
        choices=REDES_SOCIAIS,
        default='diagram-2-fill',
        max_length=50,
        blank=True,
        null=True,
    )

    url = models.CharField(
        default='https://www.instagram.com/samuelbarbosa_dev/',
        max_length=500,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.add_redeSocial.email


# ==================== Sobre ====================
class Sobre(models.Model):
    nome = models.CharField(
        max_length=50,
        default='Qual é o seu nome?',
        blank=True,
        null=True,
    )

    profissão = models.CharField(
        max_length=50,
        default='Qual é sua profissão?',
        blank=True,
        null=True,
    )

    resumo = models.CharField(
        max_length=5000,
        default='Fale um pouco sobre você.',
        blank=True,
        null=True,
    )

    foto_de_perfil = models.FileField(
        default='default/images/foto_de_perfil.svg',
        upload_to='sobre/images/',
    )

    frase = models.CharField(
        default='Qual é a sua frase?',
        max_length=50,
    )

    data_de_criação = models.DateTimeField(
        'Data de criação',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    def __str__(self):
        return self.nome


# ==================== Serviços ====================
class Servico(models.Model):
    nome = models.CharField(
        max_length=11,
        blank=True,
        null=True,
    )

    categoria = models.ForeignKey(
        PortfolioCategoria,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    preco = models.CharField(
        max_length=11,
        blank=True,
        null=True,
    )

    data_de_criação = models.DateTimeField(
        'Data de criação',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    def __str__(self):
        return self.nome

# ==================== FormularioDeContato ====================

class FormularioDeContato(models.Model):
    nome = models.CharField(
        max_length=150,
    )

    email = models.EmailField(
        max_length=600,
    )

    titulo = models.CharField(
        max_length=200,
    )

    mensagem = models.TextField(
        max_length=5000,
    )

    data_de_criação = models.DateTimeField(
        'Data de criação',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    @admin.display(
        boolean=True,
        ordering='data_de_criação',
        description='Data de criação',
    )
    def foi_publicado_recentemente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data_de_criação <= now

    def __str__(self):
        return self.nome
