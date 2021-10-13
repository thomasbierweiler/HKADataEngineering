import time
import numpy as np
import paho.mqtt.client as mqtt

client=mqtt.Client(client_id="HKA-mqtt-client")
client.connect("localhost",1883,60)
# array of integer values
vals=np.array([32,46,-33,468,983,2394,22,-5],dtype=np.int16)
print("Type of values: {}.".format(vals.dtype))
b=vals.tobytes()
client.publish("topic/test","Value 1",retain=False)
client.publish("msg/binary",payload=b,retain=False)
client.publish("topic/test","Value 2",retain=False)
print("Sleeping for 10 s")
time.sleep(10)
print("Disconnecting.")
client.publish("topic/test/3","Disconnecting",retain=False)
client.disconnect()