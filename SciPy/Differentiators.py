import numpy as np
import matplotlib.pyplot as plt
def fourPtCenteredDiff(x,y):
    """ Returns the four point centered difference of y=f(x) w.r.t x. Takes 1-dim numpy arrays for x and y """
    dydx = np.zeros(y.shape,float)
    
    dydx[2:-2] = (y[0:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:]) / (12*abs(x[1]-x[0]))
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) #2pt forward difference
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) #2pt backward difference
    dydx[1] = (y[2] - y[0])/(x[2] - x[0]) #2pt center difference
    dydx[-2] = (y[-1] - y[-3])/(x[-1] - x[-3]) #2pt center difference
    return dydx
def twoPtForwardDiff(x,y):
    """ Returns the two-point forward difference of arrays y=f(x) at x. Takes 1-dim numpy arrays for x and y """    
    dydx = np.zeros(y.shape,float) #we know it will be this size

    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx
        
def twoPtCenteredDiff(x,y):
    """ Returns the two-point centered difference of arrays y=f(x) at x. Takes 1-dim numpy arrays for x and y """
    dydx = np.zeros(y.shape,float) #we know it will be this size

    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2]) #center difference

    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx