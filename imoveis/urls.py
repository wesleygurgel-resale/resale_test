from django.urls import path

from . views import ImovelAPIView, ImobiliariaAPIView

urlpatterns = [
    # Rotas para API VIEW
    path('imobiliarias/', ImobiliariaAPIView.as_view(), name='imobiliarias'),
    path('imoveis/', ImovelAPIView.as_view(), name='imoveis'),
]