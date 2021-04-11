from django.urls import path, include
from rest_framework import routers
from .views import SensorViewSet

router = routers.DefaultRouter()
router.register(r'sensor', SensorViewSet)

urlpatterns = [
    path("", include(router.urls))
]