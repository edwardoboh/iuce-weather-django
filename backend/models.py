from django.db import models

class SensorModel(models.Model):
    temperature = models.CharField("Temperature", max_length=10)
    pressure = models.CharField("Pressure", max_length=10)
    humidity = models.CharField("Humidity", max_length=10)
    light = models.CharField("Light Intensity", max_length=10)
    created = models.DateTimeField(auto_now_add=True)