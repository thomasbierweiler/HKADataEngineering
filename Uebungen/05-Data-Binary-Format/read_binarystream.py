import pyodbc
import numpy as np
import datetime

server = 'md2c0gdc' 
database = 'HSKA_BinaryData' 
username = 'sa' 
password = 'KWmz6QOHDPLIPqzJD9t2' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# select query for all assets
# use numpy to convert the stream
cursor.execute("SELECT TOP 1 * FROM [timeseries_c464e3fe9e76lcsstream]")
row=cursor.fetchone() 
print('Fetched data with Id {}, timestamp {}, UUID {} and streamlength {}.'.format(row[0],row[1],row[2],row[3]))
print('Content of stream:')

# use numpy to convert the stream
cursor.execute("SELECT * FROM [timeseries_c464e3fe9e76lcsstream]")
count=0
s1=datetime.datetime.now()
row=cursor.fetchone()
while row:
    bdata=row[4]
    valuesnp=np.frombuffer(bdata,dtype=np.int16)
    row=cursor.fetchone()
    count=count+1
s2=datetime.datetime.now()
print('Elapsed with numpy for converting {} streams: {}'.format(count,s2-s1))
print('First 5 values of last stream:')
print(valuesnp[0:5])

# use from_bytes to convert data
cursor.execute("SELECT * FROM [timeseries_c464e3fe9e76lcsstream]")
count=0
f1=datetime.datetime.now()
row=cursor.fetchone()
while row:
    bdata=row[4]
    nlen=int(len(bdata)/2)
    valuesnp2=np.zeros((nlen,),dtype=np.int16)
    for i in range(nlen):
        valuesnp2[i]=int.from_bytes(bdata[i*2:i*2+2],byteorder='little',signed=True)
    row=cursor.fetchone()
    count=count+1
f2=datetime.datetime.now()
f=f2-f1
s=s2-s1
print('Elapsed with from_bytes for converting {} streams: {}'.format(count,s2-s1))
print('First 5 values of last stream:')
print(valuesnp2[0:5])
print('#############################################')
print('Using int.from_bytes in a loop is {:.0f} times slower than using np.frombuffer.'.format(f/s))
print('#############################################')
