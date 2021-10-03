import sys
import pandas as pd
df=pd.read_csv('Zeitreihe2.csv')
print('Erster Zeitstempel: {}'.format(df.at[1,'timestamp']))
print('Format des Zeitstempels: {}'.format(df['timestamp'].dtype))
try:
    print('Differenz der Zeitstempel: {}'.format(df['timestamp'].diff()))
except Exception as exc:
    print('An error occurred: {}'.format(exc))
# Umwandlung des "objects" in ein Zeitformat:
df.drop(0,inplace=True,axis=0)
df['timestamp']=pd.to_datetime(df['timestamp'],format='%Y-%m-%dT%H:%M:%S.%f')
print('Nach Umwandlung in ein Datumsformat:')
print('Erster Zeitstempel: {}'.format(df.at[1,'timestamp']))
print('Differenz der Zeitstempel: {}'.format(df['timestamp'].diff()))
print('Format des Zeitstempels: {}'.format(df['timestamp'].dtype))
print('Done')
