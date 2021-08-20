from .models import Imovel, Imobiliaria
from .serializers import ImovelSerializer, ImobiliariaSerializer

from rest_framework import generics
from rest_framework.generics import get_object_or_404


# LIST - CREATE ------------------------------------------------------------------------------------------------------

class ImobiliariaAPIViewListCreate(generics.ListCreateAPIView):
    """
       Imobiliarias Cadastradas List/Create
    """
    queryset = Imobiliaria.objects.all()
    serializer_class = ImobiliariaSerializer


class ImovelAPIViewListCreate(generics.ListCreateAPIView):
    """
           Imoveis Cadastrados List/Create
    """
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

    def get_queryset(self):
        if self.kwargs.get('imobiliaria_pk'):
            return self.queryset.filter(imobiliaria_id=self.kwargs.get('imobiliaria_pk'))
        return self.queryset.all()


# RETRIEVE - UPDATE - DESTROY ---------------------------------------------------------------------------------

class ImobiliariaAPIViewRUD(generics.RetrieveUpdateDestroyAPIView):
    """
       Imobiliarias Cadastradas Retrieve/Update/Destroy
    """
    queryset = Imobiliaria.objects.all()
    serializer_class = ImobiliariaSerializer


class ImovelAPIViewRUD(generics.RetrieveUpdateDestroyAPIView):
    """
        Imoveis Cadastrados Retrieve/Update/Destroy
    """
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

    def get_object(self):
        if self.kwargs.get('imobiliaria_pk'):
            return get_object_or_404(self.get_queryset(), imobiliaria_id=self.kwargs.get('imobiliaria_pk'),
                                     pk=self.kwargs.get('imovel_pk'))

        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('imovel_pk'))

