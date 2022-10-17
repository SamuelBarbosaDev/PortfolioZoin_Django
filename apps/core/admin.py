from django.contrib import admin
from core.models import *


# ==================== PORTFOLIO ====================
class PortfolioImageAdmin(admin.StackedInline):
    model = PortfolioImagem
    extra = 0

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageAdmin]
    list_display = ('titulo',)

    class Meta:
        model = Portfolio


@admin.register(PortfolioCategoria)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('categoria',)

    class Meta:
        model = PortfolioCategoria

# ==================== Contato ====================
class ContatoRedeSocialAdmin(admin.StackedInline):
    model = ContatoRedeSocial
    extra = 0

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    inlines = [ContatoRedeSocialAdmin]
    list_display = ('email',)

    class Meta:
        model = Contato

# ==================== Sobre ====================
@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('nome',)

    class Meta:
        model = Sobre

# ==================== Servicos ====================
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):

    class Meta:
        model = Servico

# ==================== FormularioDeContato ====================
@admin.register(FormularioDeContato)
class FormularioDeContatoAdmin(admin.ModelAdmin):

    class Meta:
        model = FormularioDeContato