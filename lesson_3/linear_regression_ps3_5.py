import numpy as np
import pandas as pd
import pandas
import statsmodels.api as sm
import pprint

"""
In this question, you need to:
1) implement the linear_regression() procedure
2) Select features (in the predictions procedure) and make predictions.

"""

def linear_regression(features, values):
    """
    Perform linear regression given a data set with an arbitrary number of features.
    
    This can be the same code as in the lesson #3 exercise.
    """
    
    Y = values
    X = features
    X = sm.add_constant(X)
    model = sm.OLS(Y, X)
    results = model.fit()
    #print results.summary()
    intercept, params = results.params[0], results.params[1:]
    print "Our params"
    pprint.pprint(params)
    
    return intercept, params

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with gradient descent.
    
    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv    
    
    Your prediction should have a R^2 value of 0.40 or better.
    You need to experiment using various input features contained in the dataframe. 
    We recommend that you don't use the EXITSn_hourly feature as an input to the 
    linear model because we cannot use it as a predictor: we cannot use exits 
    counts as a way to predict entry counts. 
    
    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subet (~10%) of the data contained in 
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with 
    this exercise on your own computer, locally. If you do, you may want to complete Exercise
    8 using gradient descent, or limit your number of features to 10 or so, since ordinary
    least squares can be very slow for a large number of features.
    
    If you receive a "server has encountered an error" message, that means you are 
    hitting the 30-second limit that's placed on running your program. Try using a
    smaller number of features.
    '''
    # Select Features (try different features!)
    #features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']]
    # Good R^2 = 0.479614674569
    #features = dataframe[['rain', 'precipi', 'Hour', 'mintempi']]
    # Better R^2 = 0.480976283212
    features = dataframe[['rain', 'Hour', 'mintempi', 'meandewpti', 'mindewpti']]
    # Add UNIT to features using dummy variables
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    
    # Values
    values = dataframe['ENTRIESn_hourly']
    
    # Get the numpy arrays
    features_array = features.values
    values_array = values.values

    # Perform linear regression
    intercept, params = linear_regression(features_array, values_array)
    
    predictions = intercept + np.dot(features_array, params)
    return predictions


if __name__ == "__main__":
    turnstile_weather = pd.read_csv('turnstile_data_master_with_weather.csv')
    predictions(turnstile_weather)