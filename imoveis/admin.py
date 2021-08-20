from django.contrib import admin

from .models import Imobiliaria, Imovel


@admin.register(Imobiliaria)
class ImobiliariaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'criacao', 'atualizacao']


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ['imobiliaria', 'nome', 'endereco', 'tipo', 'finalidade', 'ativo']
