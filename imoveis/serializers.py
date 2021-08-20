from rest_framework import serializers
from .models import Imobiliaria, Imovel


class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = (
            'id',
            'imobiliaria',
            'nome',
            'endereco',
            'tipo',
            'finalidade',
            'descricao',
            'caracteristica',
            'criacao',
            'ativo'
        )


class ImobiliariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imobiliaria
        fields = (
            'id',
            'nome',
            'endereco',
            'criacao',
            'atualizacao'
        )
