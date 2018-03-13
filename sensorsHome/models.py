from django.db import models
from django.utils import  timezone

# Create your models here
class Sensor(models.Model): #the base class for the app
    sensor_name = models.CharField(max_length = 100, unique = True, primary_key = True)
    sensor_type = models.CharField(max_length = 100, default = 'sensor')
    date_created = models.DateTimeField('date and time created', auto_now_add = True)
    ip_address = models.GenericIPAddressField(default = '0.1.2.3')
    sensor_text = models.CharField(max_length = 200, default = 'text')

    def __str__(self):
        return self.sensor_name

###############################################################################
#add sensor detail type model here

class DHT11_readings(models.Model):
    DHT11 = models.ForeignKey(Sensor, on_delete = models.CASCADE)
    timestamp = models.DateTimeField('date and time of reading', unique = True,
                                    primary_key = True, default = timezone.now)
    temperature = models.FloatField(default = -1000)
    humidity = models.FloatField(default = -1000)

    def __str__(self):
        return '%s Degrees and %s Humidity at %s' % (self.temperature, self.humidity,
                                                    timezone.localtime(self.timestamp))

class TSL2561_readings(models.Model):
    TSL2561 = models.ForeignKey(Sensor, on_delete = models.CASCADE)
    timestamp = models.DateTimeField('date and time of reading', unique = True,
                                    primary_key = True, default = timezone.now)
    lux = models.FloatField(default = -1000)

    def __str__(self):
        return '%s Lux at %s' % (self.lux, timezone.localtime(self.timestamp))
