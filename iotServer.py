#purpose of this script is to open up a socket on my Raspberry pi
#it will then listen for information set from the wireless sensor network
#hi everyone

##############################################################################
#import modules here
import socket
import sys
import _thread
import datetime
import sqlite3
import os
import pytz

##############################################################################
#define functions here

#function for handling connections. this will be used to create threads
def clientthread(conn,addr,dbName):
    #sending message to connected clientthread
    conn.send(bytes('Welcome, what kind of sensor are you?','utf-8'))

    #infinite loop so that functions do not terminate and thread does not end
    while True:

        #receiving from client
        data_list = ['nan']
        data = conn.recv(1024)
        dataDecoded = data.decode('utf-8')
        dataList = dataDecoded.split(',')

        #choosing function to Run
        sensorName = str(dataList[1])
        if sensorName in sensorDict:
            sensorDict[sensorName](dataList,addr,dbName)
        else:
            raise Exception('Function %s not implemented' %sensorName)

        conn.send(bytes("Thank you", 'utf-8'))

    #came out of loop
    conn.close()

#function for DHT11 Temp/humidity sensors
def DHT11_read(dataList,addr,dbName):

    #gather Django models
    from sensorsHome.models import Sensor, DHT11_readings
    from django.utils import timezone

    #Gather time information
    #timezone = pytz.timezone('US/Central')
    #timeStamp = datetime.datetime.now(tz = timezone)
    timeStamp = timezone.now()

    #gather meta-data
    sensorName = dataList[0]
    sensorType = dataList[1]
    ipAddress = addr
    temp_f = dataList[2]
    humidity = dataList[3]

    text_string = 'This sensor takes reading of temperature (F) and relative humidity (%)'

    try:
        current_sensor, sensor_created = Sensor.objects.update_or_create(
        sensor_name = sensorName, sensor_type = sensorType,
        defaults = {
        'ip_address' : ipAddress,
        'sensor_text' : text_string
        }
        )
        print('reading received from ' + str(current_sensor.sensor_name))
        current_sensor.save()
    except Exception as e:
        raise e

    try:
        current_reading = current_sensor.dht11_readings_set.create(
        timestamp = timeStamp,
        temperature = temp_f,
        humidity = humidity
        )
        print(current_reading.DHT11_id, "_", current_reading.timestamp)

    except Exception as e:
        raise e

#function for TSL2561 Light sensors
def TSL2561_read(dataList,addr,dbName):

    #gather Django models
    from sensorsHome.models import Sensor, TSL2561_readings
    from django.utils import timezone

    #Gather time information
    #timezone = pytz.timezone('US/Central')
    #timeStamp = datetime.datetime.now(tz = timezone)
    timeStamp = timezone.now()

    #gather meta-data
    sensorName = dataList[0]
    sensorType = dataList[1]
    ipAddress = addr
    light = dataList[2]

    text_string = 'This sensor takes reading of Light (lux)'

    try:
        current_sensor, sensor_created = Sensor.objects.update_or_create(
        sensor_name = sensorName, sensor_type = sensorType,
        defaults = {
        'ip_address' : ipAddress,
        'sensor_text' : text_string
        }
        )
        print('reading received from ' + str(current_sensor.sensor_name))
        current_sensor.save()
    except Exception as e:
        raise e

    try:
        current_reading = current_sensor.tsl2561_readings_set.create(
        timestamp = timeStamp,
        lux = light
        )
        print(current_reading.TSL2561_id, "_", current_reading.timestamp)

    except Exception as e:
        raise e
    #django code####################


def test_read(dataList):
    for data in dataList:
        print(data)
##############################################################################
#set up

#set up django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iotSite.settings")
import django
django.setup() #start django

#set up global variables
sensorDict = {'DHT11':DHT11_read,
            'TSL2561':TSL2561_read,
            'test': test_read}
dbName = "testTempDatabase.s3db"

#set up variables for the socket
Host = '' #symbolic name meaning all available interfaces
Port = 8888 #arbitrary non-privileged port

#start socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print( 'Socket created.')

#bind socket to specified host and specified port number
try:
    s.bind((Host, Port))

except(socket.error):
    print('Bind failed')
    sys.exit()
print('Socket bind complete')

#start listening on socket w/ backlog of 10
s.listen(10)
print('Socket is now listening')

##############################################################################
#Run server using this while loop
while 1:

    #wait to accept a connection - blocking call
    conn,addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    #start new thread takes 1st argument as a function name to be run, second is
    #the tuple of arguments to the function
    _thread.start_new_thread(clientthread, (conn,addr[0],dbName))
