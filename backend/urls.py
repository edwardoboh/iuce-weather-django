# from django.urls import path, include
# from rest_framework import routers
# from .views import SensorViewSet

# router = routers.DefaultRouter()
# router.register(r'sensor', SensorViewSet)

# urlpatterns = [
#     path("", include(router.urls))
# ]

from django.urls import path, include
from .views import SensorView
from .views import WeatherView

urlpatterns = [
    path("sensor/", SensorView.as_view()),
    path("weather/", WeatherView.as_view()),
    path("weather/<int:weather>/", WeatherView.as_view())
]