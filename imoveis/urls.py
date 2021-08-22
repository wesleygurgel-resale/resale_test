from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from .views import ImovelViewSet, ImobiliariaViewSet


router = DefaultRouter()
router.register('imobiliarias', ImobiliariaViewSet)
router.register('imoveis', ImovelViewSet)

urlpatterns = [

]