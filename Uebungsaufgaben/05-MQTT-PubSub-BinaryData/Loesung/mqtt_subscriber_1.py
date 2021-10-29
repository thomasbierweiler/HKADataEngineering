# receive sensor information and store the data to database 1 (storage of binary data)

from datetime import datetime
import numpy as np
import paho.mqtt.client as mqtt
import pyodbc

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sens1/binary")
    client.message_callback_add("sens1/binary",on_binary)

def on_message(client, userdata, msg):
    cnt=msg.payload.decode()
    print('Received message {}'.format(cnt))

def on_binary(client, userdata, msg):
    # store time when message was received
    receivetime=datetime.now()
    # first 8 bytes are the time stamp
    ts=msg.payload[:8]
    # remaining bytes contain the measurement values
    b=msg.payload[8:]
    # create POSIX timestamp from binary data
    timestamp=np.frombuffer(ts,dtype=np.float64)[0]
    # convert POSIX timestamp to datetime
    measurementtime=datetime.fromtimestamp(timestamp)
    # save to sql-database
    to_sql(measurementtime,receivetime,b)

server='md2c0gdc' 
database='MQTT-Beschleunigung' 
username='sa' 
password='KWmz6QOHDPLIPqzJD9t2' 
cnxn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor=cnxn.cursor()

def to_sql(measurementtime,receivetime,b):
    try:
        cursor.execute("INSERT INTO Messwerte_Rohformat(StartMessung,EmpfangNachricht,Rohsignal) VALUES (?,?,?)",measurementtime,receivetime,b)
        cnxn.commit()
    except:
        print("Insert to SQL Server failed.")

# name of client - must be unique
client=mqtt.Client(client_id="Subscriber1")
client.connect("localhost",1883,60)

client.on_connect=on_connect
client.on_message=on_message

client.loop_forever()