# download mosquitto broker https://mosquitto.org/download/
# start mosquitto broker with default configuration
# https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/
# package paho-mqtt
import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
  cnt=msg.payload.decode()
  print('Received message {}'.format(cnt))
  if cnt=="Done":
    print("Done!")
    client.disconnect()
    
client=mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect=on_connect
client.on_message=on_message

client.loop_forever()