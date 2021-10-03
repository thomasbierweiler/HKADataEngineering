import csv
import datetime
from datetime import date

with open('Zeitreihe1.csv') as fm:
    dt1=None
    myreader=csv.DictReader(fm)
    print(myreader.fieldnames)
    for row in myreader:
        print('Id: {}'.format(row['Id']))
        print('Datentyp der Id: {}'.format(type(row['Id'])))
        print('Umwandlung in integer: {}'.format(type(int(row['Id']))))
        print('timestamp: {}'.format(row['timestamp']))
        print('Datentyp des Zeitstempels: {}'.format(type(row['timestamp'])))
        dt2=datetime.datetime.strptime(row['timestamp'],'%Y-%m-%dT%H:%M:%S.%f')
        print('Konvertierung in ein Datum: {}'.format(dt2))
        if dt1 is None:
            dt1=dt2
        print('Differenz zum vorherigen Zeitstempel: {}'.format(dt2-dt1))
        dt1=dt2

    for row in myreader:
        print('timestamp: {}'.format(row['timestamp']))