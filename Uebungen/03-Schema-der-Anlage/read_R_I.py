import pyodbc

server = 'md2c0gdc' 
database = 'HSKA_Anlagenschema' 
username = 'sa' 
password = 'KWmz6QOHDPLIPqzJD9t2' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# select query for all assets
cursor.execute("SELECT * FROM [Assets_R_I]") 
row = cursor.fetchone() 
while row: 
    print('ID {} hat den Typ {} mit dem Anlagenkennzeichen {}.'.format(row[0],row[1],row[2]))
    row = cursor.fetchone()

# select query for all connections
cursor.execute("SELECT [AKZ1],[AKZ2] FROM [ist_verbunden_mit]") 
row = cursor.fetchone() 
while row: 
    print('{} ist verbunden mit {}.'.format(row[0],row[1]))
    row = cursor.fetchone()
print()

# select query for all connections of vessel VE1000
cursor.execute("SELECT [AKZ1],[AKZ2] FROM [ist_verbunden_mit] WHERE AKZ1='VE1000' OR AKZ2='VE1000'") 
row = cursor.fetchone() 
while row: 
    print('{} ist verbunden mit {}.'.format(row[0],row[1]))
    row = cursor.fetchone()

# select query for all connections of pump PL1100
print()
cursor.execute("SELECT [AKZ1],[AKZ2] FROM [ist_verbunden_mit] WHERE AKZ1='PL1100' OR AKZ2='PL1100'") 
row = cursor.fetchone() 
while row: 
    print('{} ist verbunden mit {}.'.format(row[0],row[1]))
    row = cursor.fetchone()