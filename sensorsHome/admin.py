from django.contrib import admin

# Register your models here.
from .models import Sensor, DHT11_readings

admin.site.register(Sensor)
admin.site.register(DHT11_readings)
