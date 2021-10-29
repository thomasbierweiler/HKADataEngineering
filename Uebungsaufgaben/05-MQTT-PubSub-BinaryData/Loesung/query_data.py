from datetime import timedelta
import pyodbc
import numpy as np
import pandas as pd
from timeit import default_timer as timer

server='md2c0gdc' 
database='MQTT-Beschleunigung' 
username='sa' 
password='KWmz6QOHDPLIPqzJD9t2' 
cnxn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#cnxn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor=cnxn.cursor()

# query data from table Messwerte_Rohformat
# get minimal time
mintime=cursor.execute('SELECT MIN(StartMessung) FROM [MQTT-Beschleunigung].[dbo].[Messwerte_Rohformat]')\
    .fetchone()[0]
start1= timer()
# select all data in minute 3
querystr="SELECT [StartMessung],[EmpfangNachricht],[Rohsignal] \
    FROM [MQTT-Beschleunigung].[dbo].[Messwerte_Rohformat] \
    WHERE [StartMessung] >= '{}' AND [StartMessung] < '{}' \
    ORDER BY [StartMessung]".format((mintime+timedelta(minutes=3)).isoformat(),(mintime+timedelta(minutes=4)).isoformat())
rows=cursor.execute(querystr).fetchall()

for row in rows:
    sm=row[0]
    en=row[1]
    rs=row[2]
    # decode data
    data=np.frombuffer(rs,dtype=np.int16)
el1=timer()-start1
# query data from table Messwerte_Einzeln
# get minimal time
mintime2=cursor.execute('SELECT MIN(StartMessung) FROM [MQTT-Beschleunigung].[dbo].[Messwerte_Einzeln]')\
    .fetchone()[0]
start2=timer()
# select all data in minute 3
querystr="SELECT [StartMessung],[EmpfangNachricht],[ZeitstempelMesswertErzeugung],[Messwert],[IdentifierDesPakets] \
    FROM [MQTT-Beschleunigung].[dbo].[Messwerte_Einzeln] \
    WHERE [StartMessung] >= '{}' AND [StartMessung] < '{}' \
    ORDER BY [StartMessung]".format((mintime2+timedelta(minutes=3)).isoformat(),(mintime2+timedelta(minutes=4)).isoformat())
# rows=cursor.execute(querystr).fetchall()
# extract data from cursor
df=pd.read_sql_query(querystr,cnxn)
# group data by IdentifierDesPakets
dfg=df.groupby(['IdentifierDesPakets'],sort=False)
el2=timer()-start1
# we've got 60 groups (one per second)
print('Number of groups: {}'.format(dfg.ngroups))
# summary
print('Elapsed time in seconds for querying table 1 and extracting data: {}'.format(el1))
print('Elapsed time in seconds for querying table 2 and extracting data: {}'.format(el2))
if el1 > 0.0:
    print('Extracting data from binary data is {} times faster.'.format(round(el2/el1,1)))
