from django_filters import rest_framework as filters

from .models import Imovel, Imobiliaria


class ImobiliariaFilter(filters.FilterSet):
    class Meta:
        model = Imobiliaria
        fields = ['nome']


class ImovelFilter(filters.FilterSet):
    class Meta:
        model = Imovel
        fields = ['nome', 'tipo', 'imobiliaria']
