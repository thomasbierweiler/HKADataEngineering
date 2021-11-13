# introduction to lmfit, see https://lmfit.github.io/lmfit-py/examples/example_use_pandas.html#sphx-glr-examples-example-use-pandas-py

import os
import db_gp as db

# class information generated by proto compiler
import mathfunc_pb2

class FGuesserGP:
    def __init__(self) -> None:
        pass

    def guess_gp(self,config,function_id:int)->mathfunc_pb2.State:
        # check if result exists
        state=db.get_status(config,function_id)
        # check if calculation has to be scheduled
        if not state.scheduled and not state.resultready:
            # update db entry
            db.set_status_scheduled(config,function_id)
            # guess function
            fnc=self._guess_gp(config,function_id)
            # update db entry
            db.gpmodel_todb(config,function_id,fnc)
            state.scheduling=True            
        return state

    def _guess_gp(self,config,function_id:int)->str:
        # start DEAP as separate program
        # read data as df and save it to disc
        df=db.get_datapoints(config,function_id)
        df.to_pickle(".\data\datapoints{}.pkl".format(function_id))
        os.system("python gp_deap.py {}".format(function_id))
        print('Done with gp_deap.py')
        # read result from file
        with open('.\data\sympy_term{}.txt'.format(function_id),"r") as f:
            fnc=f.readline()
            print('FGuesserGP: Function determined by GP: {}'.format(fnc))
        return fnc