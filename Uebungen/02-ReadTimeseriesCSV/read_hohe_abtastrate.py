import pandas as pd

# specify filename
fn='Zeitreihe-hohe-Abtastrate.csv'
# open file
with open(fn) as fm:
    fm.readline() # ignore first line
    ct=fm.readline() # read second line with timestamp and sampling rate
    vals=ct.split(';')
    print('Starting time: {}, sampling rate: {}'.format(vals[2],vals[3]))
# file handle is automatically close
# read data into dataframe, starting with row# 3
df=pd.read_csv(fn,skiprows=2,delimiter=';')
# construct time stamp
df['timestamp']=vals[2]
# convert timestamp (string) to datetime format
df['timestamp']=pd.to_datetime(df['timestamp'],format='%Y-%m-%dT%H:%M:%S.%f')
# convert sampling rate to seconds
sp=1.0/float(vals[3])
# add sampling rate to timestamp
# offset in secconds
offset=(df['number']-1)*sp
df['offset']=offset
df['offset']=df['offset']*1e9 # multiply with 1e9 -> nanoseconds are expected
df['offsetAsTime']=df['offset'].astype('timedelta64[ns]')
df['timestampWithOffset']=df['timestamp'].add(df['offsetAsTime'])
print(df.head())
print('Done')