from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from imoveis.urls import router

urlpatterns = [
    # Authentication
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # Views and Routers
    path('', RedirectView.as_view(url='/api/v1/')),
    path('api/v1/', include(router.urls)),

    # Schema
    path('schema', get_schema_view(
        title="Resale API",
        description="API for the real estate market…",
        version="1.0.0"
    ), name='openapi-schema'),

    # Docs
    path('docs/', include_docs_urls(title='ResaleAPI')),
]
