import numpy as np
import datetime

class sensorsystem:
    def __init__(self, min_raw_value:np.int16,max_raw_value:np.int16, min_value_g:np.float64, max_value_g:np.float64):
        self._min_raw_value=min_raw_value
        self._max_raw_value=max_raw_value
        self._min_value_g=min_value_g
        self._max_value_g=max_value_g
        self._starttime=datetime.datetime.now()
        self._f_Hz:np.float64=1.0
        self._amplitude_g:np.float64=1.0
        self._noise_g:np.float64=0.01
        self._method=np.sin
        self._samplingrate=1.0

    # starttime of measurement function    
    @property
    def starttime(self)->datetime.datetime:
        return self._starttime

    @starttime.setter
    def starttime(self, value:datetime.datetime):
        self._starttime=value

    # frequency in Hertz
    @property
    def f_Hz(self)->np.float64:
        return self._f_Hz

    @f_Hz.setter
    def f_Hz(self, value:np.float64):
        self._f_Hz=value

    # amplitude in g
    @property
    def amplitude_g(self)->np.float64:
        return self._amplitude_g

    @f_Hz.setter
    def amplitude_g(self, value:np.float64):
        self._amplitude_g=value

    # noise in g
    @property
    def noise_g(self)->np.float64:
        return self._noise_g

    @noise_g.setter
    def noise_g(self, value:np.float64):
        self._noise_g=value

    # measurement function
    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        self._method=value

    # samplingrate
    @property
    def samplingrate(self)->np.float64:
        return self._samplingrate

    @samplingrate.setter
    def samplingrate(self,value):
        self._samplingrate=value

    # measurement value in g -> raw value
    def value_g_to_raw(self,value_g):
        return self._max_raw_value/self._max_value_g*value_g

    # return a specified number of measurement values at a given timestamp
    def get_raw_measurement_values(self,timestamp:datetime.datetime,nof_values):
        s=timestamp-self._starttime
        # calculate the argument of the sinus
        phi=2*np.pi*self._f_Hz
        # amplitude as raw value
        A=self.value_g_to_raw(self._amplitude_g)
        # start seconds
        starts=s.total_seconds()
        # create linear spacing between start seconds and (starts seconds + samples)
        # note (nof_values-1) in order to obtain the correct result
        scnds=np.linspace(starts,starts+1.0/self._samplingrate*(nof_values-1),nof_values,endpoint=True)
        # create an array of random noise (+/-0,01 g)
        R=(np.random.rand(nof_values,)*2.0-1.0)*self.noise_g
        # convert noise to raw values
        R=self.value_g_to_raw(R)
        # calculate the sin: A*sin(phi*t)
        vals=A*self._method(phi*scnds)
        # add the noise
        vals=R+vals
        # return the values as int16
        return vals.astype(np.int16)
