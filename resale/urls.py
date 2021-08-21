from django.contrib import admin
from django.urls import path, include
from imoveis.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # Rota Para URL'S- IMOVEIS - API VIEW
    # path('api/v1/', include('imoveis.urls')),
    path('api/v1/', include(router.urls)),
]
