import time
import paho.mqtt.client as mqtt

client=mqtt.Client(client_id="HKA-mqtt-client")
# set last will message
client.will_set("client/lastwill","Last will message: Connection to server lost",retain=False)
client.connect("localhost",1883,60)
client.publish("topic/test/1","Value 1",retain=False)
client.publish("topic/test/2","Value 2",retain=False)
client.publish("topic/test/3","Value 3",retain=False)
print("Sleeping for 10 s")
time.sleep(10)
print("Disconnecting.")
client.publish("topic/test/3","Disconnecting",retain=False)
client.disconnect()