import sys
from datetime import datetime
from datetime import timedelta
import time
from typing_extensions import runtime
import numpy as np
from sensorsystem import sensorsystem
import paho.mqtt.client as mqtt

# get range of int16
ii16=np.iinfo(np.int16)
# instantiate sensor system 
sensor=sensorsystem(ii16.min,ii16.max,-16.0,16.0)

# set method that the sensor measures
sensor.method=np.sin
# set frequency in Hertz
sensor.f_Hz=775.0
# set amplitude in g
sensor.amplitude_g=10
# set noise in g
sensor.noise_g=0.01
# set sampling rate of the acceleration sensor
sensor.samplingrate=10000

# instantiate the mqtt client
client=mqtt.Client(client_id="HKA-mqtt-client")
client.connect("localhost",1883,60)

# read lifetime in minutes from command line
lifetime_min=int(' '.join(sys.argv[1:]) or '10')
lifetime=timedelta(minutes=lifetime_min)
start=datetime.now()
runnertime=timedelta(seconds=0)
while datetime.now()-start<lifetime:
    # get current time (time when measurement starts)
    current=datetime.now()
    # get 1024 measurement values at current time
    vals=sensor.get_raw_measurement_values(current,1024)
    # transform measurement to bytes
    b=vals.tobytes()
    # transform current time to bytes
    # first 8 bytes: timestamp; all other bytes contain the measurement values
    b=np.float64(current.timestamp()).tobytes()+b
    # publish data
    client.publish('sens1/binary',payload=b,retain=False)
    # sleep remaining time (of a second)
    td=timedelta(seconds=1)-(datetime.now()-(start+runnertime))
    #print('Sleeping for {} s'.format(td.total_seconds()))
    if td>timedelta(0):
        time.sleep(td.total_seconds())
    # increase time of loop by 1 second
    runnertime+=timedelta(seconds=1)
