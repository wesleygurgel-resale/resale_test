from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ImovelViewSet, ImobiliariaViewSet


router = SimpleRouter()
router.register('imobiliarias', ImobiliariaViewSet)
router.register('imoveis', ImovelViewSet)

urlpatterns = [

]