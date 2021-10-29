from datetime import datetime, timedelta
import numpy as np
import paho.mqtt.client as mqtt
import pyodbc

server='md2c0gdc' 
database='MQTT-Beschleunigung' 
username='sa' 
password='KWmz6QOHDPLIPqzJD9t2' 
cnxn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor=cnxn.cursor()

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
    # decode binary data
    cnt=np.frombuffer(b,np.int16)
    # get maximal group counter
    cursor.execute('SELECT MAX(IdentifierDesPakets) FROM [MQTT-Beschleunigung].[dbo].[Messwerte_Einzeln] ')
    grpCnt=0
    for row in cursor.fetchone():
        if row is not None:
            grpCnt=row+1
    # save each measurement value to sql-database
    for i in range(cnt.shape[0]):
        # sampling rate: 10000 Hz
        to_sql(measurementtime,receivetime,cnt[i],measurementtime+timedelta(seconds=i*1/10000),grpCnt)

def to_sql(measurementtime,receivetime,cnt,timestampOfMeasurement,grpCnt):
    cursor.execute("INSERT INTO Messwerte_Einzeln(StartMessung,EmpfangNachricht,Messwert,ZeitstempelMesswertErzeugung,IdentifierDesPakets) \
        VALUES (?,?,?,?,?)",measurementtime,receivetime,int(cnt),timestampOfMeasurement,grpCnt)
    cnxn.commit()
    
# name of client - must be unique
client=mqtt.Client(client_id="Subscriber2")
client.connect("localhost",1883,60)

client.on_connect=on_connect
client.on_message=on_message

client.loop_forever()