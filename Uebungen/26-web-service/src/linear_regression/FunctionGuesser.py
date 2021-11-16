# introduction to lmfit, see https://lmfit.github.io/lmfit-py/examples/example_use_pandas.html#sphx-glr-examples-example-use-pandas-py
from lmfit.models import LinearModel
import numpy

import db_ops as db
import db_src

# class information generated by proto compiler
import mathfunc_pb2

class FunctionGuesser:
    def __init__(self) -> None:
        pass

    def guess_linear(self,config,function_id:int)->mathfunc_pb2.State:
        # check if result exists
        state=db.get_status(config,function_id)
        # check if calculation has to be scheduled
        if not state.scheduled and not state.resultready:
            # update db entry
            db.set_status_scheduled(config,function_id)
            # guess function
            fnc,rmse=self._guess_linear(config,function_id)
            # update db entry
            db.linmodel_todb(config,function_id,fnc,rmse)
            state.scheduling=True
        return state

    def _guess_linear(self,config,function_id:int)->str:
        df=db_src.get_datapoints(config,function_id)
        model=LinearModel()
        params=model.guess(df['y'],x=df['x'])
        result=model.fit(df['y'],params,x=df['x'])
        # calculate root mean square error
        rmse=self.rmse(df['y'].to_numpy(),result.best_fit)
        return 'y={}*x+{}'.format(params['slope'].value,params['intercept'].value),rmse

    # calculate the root mean squared error
    def rmse(self,estimated:numpy.ndarray,values:numpy.ndarray)->float:
        return numpy.sqrt(numpy.sum(numpy.square(estimated-values))/values.shape[0])

