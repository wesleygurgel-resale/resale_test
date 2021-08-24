from django.http import HttpRequest

from .models import Imovel, Imobiliaria
from .serializers import ImovelSerializer, ImobiliariaSerializer
from .filters import ImovelFilter, ImobiliariaFilter

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

"""
API V1
"""


class ImobiliariaViewSet(viewsets.ModelViewSet):
    """
    Imobiliária e suas propriedades.

    list:
    Retorna lista de Imobiliárias cadastrados.

    create:
    Cria uma nova instância de Imobiliária.

    retrieve:
    Retorna a Imobiliária passada como parâmetro.

    delete:
    Deleta a Imobiliária passada como parâmetro.

    update:
    Atualiza uma Imobiliária com base no seu ID.
    """

    queryset = Imobiliaria.objects.all()
    serializer_class = ImobiliariaSerializer
    filterset_class = ImobiliariaFilter

    @action(detail=True, methods=['GET'])
    def listar_imoveis(self, request: HttpRequest, pk=None):
        """
        Listar Imoveis de uma Imobiliaria específica com base em seu ID.

        :param request:
        :param pk:
        :return:
        """
        self.pagination_class.page_size = 2
        imoveis = Imovel.objects.filter(imobiliaria_id=pk)

        imoveis_filtrados = ImovelFilter(request.GET, queryset=imoveis).qs
        page = self.paginate_queryset(imoveis_filtrados)

        if page:
            serializer = ImovelSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ImovelSerializer(imoveis_filtrados, many=True)
        return Response(serializer.data)


class ImovelViewSet(viewsets.ModelViewSet):
    """
    list:
    Retorna lista de Imovéis cadastrados.

    create:
    Cria uma nova instância de Imóvel.

    retrieve:
    Retorna o Imóvel passado como parâmetro.

    delete:
    Deleta o Imóvel passado como parâmetro.

    update:
    Atualiza um Imóvel com base no seu ID.
    """
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    filterset_class = ImovelFilter

