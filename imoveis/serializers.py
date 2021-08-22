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

    def validate_descricao(self, descricao):
        """
        Validate de Descrição, verificar se a descrição é diferente da 'default'

        :param texto:
        :return:
        """
        if descricao != 'Digite aqui a descrição do Imóvel' and descricao != '':
            return descricao
        raise serializers.ValidationError('É necessário digitar uma descrição válida para o Imóvel!')


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
