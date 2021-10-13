# download mosquitto broker https://mosquitto.org/download/
# start mosquitto broker with default configuration
# https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/
# package paho-mqtt
import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("topic/test", "Done",retain=False)
client.disconnect()