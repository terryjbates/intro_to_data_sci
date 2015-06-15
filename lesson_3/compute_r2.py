import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys


def sample_variance(input_data, ):
    pass


def compute_r_squared(data, predictions):
    '''
    In exercise 5, we calculated the R^2 value for you. But why don't you try and
    and calculate the R^2 value yourself.
    
    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    '''
    
    # your code here
    # Used http://connor-johnson.com/2014/02/18/linear-regression-with-python/
    sst = np.sum((data - np.mean(data)) **2)
    ssr = np.sum((data - predictions) **2)
    
    r_squared = 1 - (ssr/sst)
    return r_squared