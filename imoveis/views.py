from .models import Imovel, Imobiliaria
from .serializers import ImovelSerializer, ImobiliariaSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

"""
API V1
"""


class ImobiliariaViewSet(viewsets.ModelViewSet):
    queryset = Imobiliaria.objects.all()
    serializer_class = ImobiliariaSerializer

    @action(detail=True, methods=['GET'])
    def listar_imoveis(self, request, pk=None):
        self.pagination_class.page_size = 1
        imoveis = Imovel.objects.filter(imobiliaria_id=pk)
        page = self.paginate_queryset(imoveis)

        if page:
            serializer = ImovelSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ImovelSerializer(imoveis, many=True)
        return Response(serializer.data)


class ImovelViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet
                    ):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
