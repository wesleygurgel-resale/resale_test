from django.urls import path

from . views import ImovelAPIViewListCreate, ImobiliariaAPIViewListCreate
from .views import ImovelAPIViewRUD, ImobiliariaAPIViewRUD

urlpatterns = [
    # Rotas para API VIEW - LIST - CREATE with Generics
    path('imobiliarias/', ImobiliariaAPIViewListCreate.as_view(), name='imobiliarias'),
    path('imoveis/', ImovelAPIViewListCreate.as_view(), name='imoveis'),

    # Rotas para API VIEW - RETRIEVE - UPDATE - DESTROY with Generics
    path('imobiliarias/<int:pk>/', ImobiliariaAPIViewRUD.as_view(), name='imobiliarias_rud'),
    path('imoveis/<int:imovel_pk>/', ImovelAPIViewRUD.as_view(), name='imoveis_rud'),

    # Rotas para Imoveis de uma Imobiliaria
    path('imobiliarias/<int:imobiliaria_pk>/imoveis/', ImovelAPIViewListCreate.as_view(), name='imobiliaria_imoveis'),
    path('imobiliarias/<int:imobiliaria_pk>/imoveis/<int:imovel_pk>/', ImovelAPIViewRUD.as_view(),
         name='imobiliaria_imoveis_rud'),

]