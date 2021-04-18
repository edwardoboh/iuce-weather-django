# from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets
# from .models import SensorModel
# from .serializers import SensorSerializer

# class SensorViewSet(viewsets.ModelViewSet):
#     queryset = SensorModel.objects.all().order_by('-created')
#     serializer_class = SensorSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SensorModel
from .serializers import SensorSerializer

class SensorView(APIView):
    def get(self, request):
        theModel = SensorModel.objects.all().order_by('-created')
        serializedData = SensorSerializer(theModel, many=True)
        return Response(serializedData.data)


class WeatherView(APIView):
    def post(self, request):
            serializedData = SensorSerializer(data=request.data)
            if serializedData.is_valid(raise_exception=True):
                serializedData.save()
                return Response(serializedData.data)
            return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, weather):
        weatherData = {
            'temperature': weather.GET.getlist('temperature')[0],
            'pressure': weather.GET.getlist('pressure')[0],
            'humidity': weather.GET.getlist('humidity')[0],
            'light': weather.GET.getlist('light')[0]
        }
        serializedWeather = SensorSerializer(data=weatherData)
        if serializedWeather.is_valid():
            serializedWeather.save()
            return Response(serializedWeather.data)
        return Response(serializedWeather.errors, status=status.HTTP_400_BAD_REQUEST)