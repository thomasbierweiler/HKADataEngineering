# build queries to find possible ways from vessel VE1000 to T-part T5

import pyodbc
# SQL server connection
server='md2c0gdc' 
database='HSKAGraphAnlagenschema' 
username='sa' 
password='KWmz6QOHDPLIPqzJD9t2' 
cnxn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor=cnxn.cursor()

#query graph database
def CnstQuery(nOfConnections:int,start:str,end:str=None)->str:
    assert nOfConnections>0, "Parameter nOfConnection must be greater than 0."
    assert start is not None, "Parameter start must be defined."
    """
    We try and build queries like the following
    SELECT CONCAT(asset1.AKZ,'->',asset2.AKZ,'->',asset3.AKZ,'->',asset4.AKZ,'->',asset5.AKZ)
        FROM Assets asset1, connectedTo c1, Assets asset2,connectedTo c2, Assets asset3,connectedTo c3, Assets asset4,connectedTo c4, Assets asset5
        WHERE MATCH(asset1-(c1)->asset2-(c2)->asset3-(c3)->asset4-(c4)->asset5)
        AND asset1.AKZ = 'VE1000' -- start
        AND asset2.AKZ != asset1.AKZ
        AND asset3.AKZ != asset2.AKZ
        AND asset4.AKZ != asset3.AKZ
        AND asset5.AKZ != asset4.AKZ
        AND asset5.AKZ = 'T5' -- end
    """
    # build query
    query="SELECT DISTINCT "
    # construct select statement
    for i in range(nOfConnections+1):
        query+='asset'+str(i)+'.AKZ,'
    # remove ,
    query=query[:-1]
    # construct FROM statement
    query+=' FROM'
    for i in range(nOfConnections):
        query+=' Assets asset'+str(i)+','
        query+='connectedTo c'+str(i)+','
    query+=' Assets asset'+str(i+1)
    # construct WHERE statement
    query+=' WHERE MATCH('
    for i in range(nOfConnections):
        query+='asset'+str(i)+'-(c'+str(i)+')->'
    # remove ->
    query+='asset'+str(nOfConnections)
    query+=')'
    # construct AND statements
    query+=" AND asset0.AKZ='{}'".format(start)
    for i in range(1,nOfConnections):
        query+=' AND asset'+str(i)+'.AKZ!=asset'+str(i-1)+'.AKZ'
    for i in range(1,nOfConnections):
        query+=' AND asset'+str(i)+'.AKZ!='+"'"+start+"'"
    if end is not None:
        query+=' AND asset'+str(nOfConnections)+'.AKZ='+"'"+end+"'"
    return query

start='VE1000'
end='T5'

# get number of connections (this is the worst case)
maxConnections=cursor.execute('SELECT COUNT(*) FROM dbo.connectedTo').fetchone()[0]
for i in range(1,maxConnections):
    query=CnstQuery(i,start,end)
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
print('Done')

