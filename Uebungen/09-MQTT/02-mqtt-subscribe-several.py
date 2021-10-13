import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic/test/#")
    client.subscribe("client/lastwill")
    client.message_callback_add("topic/test/#",on_clb)

def on_message(client, userdata, msg):
    cnt=msg.payload.decode()
    print('Received message {}'.format(cnt))
    if cnt=="Done":
        print("Done!")
        client.disconnect()

def on_clb(client, userdata, msg):
    cnt=msg.payload.decode()
    print('On_clb: Topic {}: Received message {} at time.'.format(msg.topic,cnt))
    
client=mqtt.Client(client_id="Subscriber")
client.connect("localhost",1883,60)

client.on_connect=on_connect
client.on_message=on_message

client.loop_forever()