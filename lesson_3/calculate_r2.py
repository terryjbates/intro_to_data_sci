import numpy as np

def compute_r_squared(data, predictions):
    SST = ([data-np.mean(data))**2]).sum()
    SSReg = ((predictions-data)**2).sum()
    r_squared = 1 -SSReg / SST
    
    return r_squared