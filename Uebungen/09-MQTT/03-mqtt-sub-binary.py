import numpy as np
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic/test")
    client.subscribe("msg/binary")
    client.message_callback_add("msg/binary",on_binary)

def on_message(client, userdata, msg):
    cnt=msg.payload.decode()
    print('Received message {}'.format(cnt))

def on_binary(client, userdata, msg):
    cnt=np.frombuffer(msg.payload,dtype=np.int16)
    print('Received and decoded binary message {}'.format(cnt))
    
client=mqtt.Client(client_id="Subscriber")
client.connect("localhost",1883,60)

client.on_connect=on_connect
client.on_message=on_message

client.loop_forever()