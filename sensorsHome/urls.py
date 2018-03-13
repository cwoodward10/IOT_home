from django.conf.urls import url

from . import views

app_name = 'sensorsHome'
urlpatterns = [
    #/sensors/
    url(r'^$', views.index, name = 'index'),
    #/sensors/sensor_name
    url(r'^(?P<sensor_name>Sensor-(?P<sensor_type>DHT11)-.+)/$', views.detail_dht11, name = 'detail_DHT11'),
    #/sensors/sensor_name
    url(r'^(?P<sensor_name>Sensor-(?P<sensor_type>TSL2561)-.+)/$', views.detail_tsl2561, name = 'detail_TSL2561')
]
