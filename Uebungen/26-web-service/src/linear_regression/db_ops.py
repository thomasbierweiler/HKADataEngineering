import pyodbc
import pandas as pd

# class information generated by proto compiler
import mathfunc_pb2

def create_db(config)->bool:
    drv = pyodbc.drivers()
    DRIVER_NAME=drv[3]
    SQL_STR="Driver={"+DRIVER_NAME+"};SERVER="+config['SERVER']+';UID='+config['UID']+';PWD='+config['PWD']
    cnxn = pyodbc.connect(SQL_STR, autocommit=True)
    cursor = cnxn.cursor()
    # check if db exists
    SQL_QUERY="SELECT COUNT(name) FROM sys.databases WHERE name='{}'".format(config['DBLINEARREGRESSION'])
    cursor.execute(SQL_QUERY)
    cnt = cursor.fetchone()
    if cnt[0] == 0:
        # create db
        SQL_QUERY = "CREATE DATABASE [{}]".format(config['DBLINEARREGRESSION'])
        cursor.execute(SQL_QUERY)
        cnxn.close()
        # create tables
        create_table_linearregressionresult(config)
        return True
    return False

def create_table_linearregressionresult(config):
    drv = pyodbc.drivers()
    DRIVER_NAME=drv[3]
    SQL_STR="Driver={"+DRIVER_NAME+"};SERVER="+config['SERVER']+';DATABASE='+config['DBLINEARREGRESSION']+';UID='+config['UID']+';PWD='+config['PWD']
    cnxn = pyodbc.connect(SQL_STR, autocommit=True)
    cursor = cnxn.cursor()
    SQL_QUERY="""CREATE TABLE [dbo].[linregresult](
        [Id] [int] IDENTITY(1,1) NOT NULL,
        [FunctionId] [int] NOT NULL,
        [scheduled] [bit] NOT NULL,
        [ready] [bit] NOT NULL,
        [function] [nvarchar](max) NULL
        )
        """
    cursor.execute(SQL_QUERY)
    cnxn.commit()
    cnxn.close()

def get_status(config,function_id:int)->mathfunc_pb2.State:
    state=mathfunc_pb2.State()
    state.scheduling=False
    state.scheduled=False
    state.resultready=False
    drv=pyodbc.drivers()
    DRIVER_NAME=drv[3]
    SQL_STR="Driver={"+DRIVER_NAME+"};SERVER="+config['SERVER']+';DATABASE='+config['DBLINEARREGRESSION']+';UID='+config['UID']+';PWD='+config['PWD']
    cnxn=pyodbc.connect(SQL_STR)
    cursor=cnxn.cursor()
    result=cursor.execute(
        """SELECT [scheduled],[ready] FROM [dbo].[linregresult]
            WHERE [FunctionId]=?
        """,function_id).fetchone()
    if result is None:
        pass
    elif result[0] and not result[1]: # scheduled, not ready
        state.scheduled=True
    elif not result[0] and result[1]: # ready
        state.resultready=True
    else:
        assert not (result[0] and result[1]),"in db_ops, get_status: scheduled and resultready are exclusive." # entry in db is wrong
    cnxn.close()
    return state

def get_datapoints(config,function_id:int)->pd.DataFrame:
    drv = pyodbc.drivers()
    DRIVER_NAME=drv[3]
    SQL_STR="Driver={"+DRIVER_NAME+"};SERVER="+config['SERVER']+';DATABASE='+config['DBSRC']+';UID='+config['UID']+';PWD='+config['PWD']
    cnxn=pyodbc.connect(SQL_STR)
    SQL="""SELECT [x],[y] FROM [dbo].[datapoints]
            WHERE [FunctionId]={}
            ORDER BY [x]
        """.format(function_id)
    df=pd.read_sql(SQL,cnxn)
    cnxn.close()
    return df

def set_status_scheduled(config,function_id):
    drv = pyodbc.drivers()
    DRIVER_NAME=drv[3]
    SQL_STR="Driver={"+DRIVER_NAME+"};SERVER="+config['SERVER']+';DATABASE='+config['DBLINEARREGRESSION']+';UID='+config['UID']+';PWD='+config['PWD']
    cnxn=pyodbc.connect(SQL_STR,autocommit=True)
    cnxn.cursor().execute("INSERT INTO linregresult(FunctionId,scheduled,ready) VALUES (?,?,?)",function_id,True,False)
    cnxn.close()

def linmodel_todb(config,function_id:int,fnc:str):
    drv = pyodbc.drivers()
    DRIVER_NAME=drv[3]
    SQL_STR="Driver={"+DRIVER_NAME+"};SERVER="+config['SERVER']+';DATABASE='+config['DBLINEARREGRESSION']+';UID='+config['UID']+';PWD='+config['PWD']
    cnxn=pyodbc.connect(SQL_STR,autocommit=True)
    cnxn.cursor().execute("UPDATE linregresult SET [scheduled]=?,[ready]=?,[function]=? WHERE [FunctionId]=?",False,True,fnc,function_id)
    cnxn.close()
    
def delete_fitted(config):
    drv = pyodbc.drivers()
    DRIVER_NAME=drv[3]
    SQL_STR="Driver={"+DRIVER_NAME+"};SERVER="+config['SERVER']+';DATABASE='+config['DBLINEARREGRESSION']+';UID='+config['UID']+';PWD='+config['PWD']
    cnxn=pyodbc.connect(SQL_STR,autocommit=True)
    cnxn.cursor().execute("DELETE FROM linregresult")
    cnxn.close()
