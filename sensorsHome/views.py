from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.models import Avg, Max, Min, Count
from .models import Sensor, DHT11_readings

def index(request):
    sensors_list = Sensor.objects.order_by('-date_created')[:10]

    context = {'sensors_list': sensors_list}
    return render(request, 'sensorsHome/index.html', context)

def detail_dht11(request, sensor_name,sensor_type):
    sensor = Sensor.objects.get(sensor_name = sensor_name)
    readings_list = sensor.dht11_readings_set.all().order_by('-timestamp')[:60]
    readings_count = len(sensor.dht11_readings_set.all())
    aggregate_dict = sensor.dht11_readings_set.aggregate(Avg('temperature'), Avg('humidity'),
                                            Max('temperature'), Min('temperature'),
                                            Max('humidity'), Min('humidity'))

    context = {'sensor' : sensor,
                'sensor_type' :sensor_type,
                'readings_list' : readings_list,
                'readings_count': readings_count,
                'aggregate_dict': aggregate_dict
                }
    return render(request, 'sensorsHome/detail_dht11.html', context)

def detail_tsl2561(request, sensor_name,sensor_type):
    sensor = Sensor.objects.get(sensor_name = sensor_name)
    readings_list = sensor.tsl2561_readings_set.all().order_by('-timestamp')[:60]
    readings_count = len(sensor.tsl2561_readings_set.all())
    aggregate_dict = sensor.tsl2561_readings_set.aggregate(Avg('lux'),
                                            Max('lux'), Min('lux'))

    context = {'sensor' : sensor,
                'sensor_type' :sensor_type,
                'readings_list' : readings_list,
                'readings_count': readings_count,
                'aggregate_dict': aggregate_dict
                }
    return render(request, 'sensorsHome/detail_tsl2561.html', context )
