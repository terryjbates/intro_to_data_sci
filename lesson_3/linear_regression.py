import statsmodels.api as sm

def linear_regression(features, values):
    """
    Performs linear regression given a dataset with an arbitrary number of features.
    'features' is the input data points (or the X's) and 'values' is the output data points
    (or the Y's).
    
    Returns the intercept and the parameters, that is, the optimal values of theta.
    
    This page contains example code that may be helpful:
    http://statsmodels.sourceforge.net/0.5.0/generated/statsmodels.regression.linear_model.OLS.html
    """
    Y = values
    X = features
    X = sm.add_constant(X)
    model = sm.OLS(Y,X)
    results = model.fit()
    print results.summary()
    intercept, params = results.params[0], results.params[1:]
    
    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################
    
    return intercept, params
