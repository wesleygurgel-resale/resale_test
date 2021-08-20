from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Imovel, Imobiliaria
from .serializers import ImovelSerializer, ImobiliariaSerializer


class ImobiliariaAPIView(APIView):
    """
    Imobiliarias Cadastradas!
    """

    def get(self, request):
        imobiliarias = Imobiliaria.objects.all()
        serializer = ImobiliariaSerializer(imobiliarias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImobiliariaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Verifica se é válido e manda exceção! é COndinção de parada.
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ImovelAPIView(APIView):
    """
    Imovéis Cadastrados!
    """

    def get(self, request):
        imoveis = Imovel.objects.all()
        serializer = ImovelSerializer(imoveis, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImovelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Verifica se é válido e manda exceção! é COndinção de parada.
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
