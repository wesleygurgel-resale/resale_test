from django.http import HttpRequest

from .models import Imovel, Imobiliaria
from .serializers import ImovelSerializer, ImobiliariaSerializer
from .filters import ImovelFilter, ImobiliariaFilter

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

"""
API V1
"""


class ImobiliariaViewSet(viewsets.ModelViewSet):
    """
    Para acessar imoveis: /api/v1/imoveis/
    """

    queryset = Imobiliaria.objects.all()
    serializer_class = ImobiliariaSerializer
    filterset_class = ImobiliariaFilter

    @action(detail=True, methods=['GET'])
    def listar_imoveis(self, request: HttpRequest, pk=None):
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
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    filterset_class = ImovelFilter

