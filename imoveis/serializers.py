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
            'ativo'
        )


class ImobiliariaSerializer(serializers.ModelSerializer):

    # HyperLinked Related Field
    propriedades = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='imovel-detail')

    class Meta:
        model = Imobiliaria
        fields = (
            'id',
            'nome',
            'endereco',
            'propriedades',
        )
