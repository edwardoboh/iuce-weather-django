from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import SensorModel
from .serializers import SensorSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = SensorModel.objects.all().order_by('-created')
    serializer_class = SensorSerializer