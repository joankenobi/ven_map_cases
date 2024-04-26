from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from .views import MapViewSet

router = DefaultRouter()
router.register('map', MapViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='Maps API'))
]

