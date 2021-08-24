from django.contrib import admin

from .models import Imobiliaria, Imovel, Tipo


@admin.register(Imobiliaria)
class ImobiliariaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'criacao', 'atualizacao']


@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ['tipo']


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ['imobiliaria', 'nome', 'endereco', 'tipo', 'finalidade', 'ativo']
