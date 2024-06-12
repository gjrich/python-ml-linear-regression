################################
# Import Packages First
################################

# Python Standard Library Packages
import random
import statistics
from typing import List, Tuple

# External Packages (must be installed)
# Use requirements.txt and list 
# One package per line

import numpy as np
from scipy import stats
import statsmodels.api as sm

# Import the LinearRegression class from scikit-learn
from sklearn.linear_model import LinearRegression

################################
# Define Functions
################################

def std_lib_statistics_linear_regression(xlist: List[float], ylist: List[float]) -> Tuple[float, float]:
    # Fit linear regression model given our x and y lists
    slope, intercept = statistics.linear_regression(xlist, ylist)
    return slope, intercept

def statsmodels_linear_regression(X: List[float], y: List[float]) -> str:
    X = sm.add_constant(X)  # Adds intercept term
    model = sm.OLS(y, X).fit()
    return model.summary()


def numpy_linear_regression(X: List[float], y: List[float]) -> Tuple[float, float]:
    X = np.array(X)
    y = np.array(y)
    X = np.vstack([np.ones(len(X)), X]).T  # Adds intercept term
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
    return theta[1], theta[0]  # Returns slope, intercept


def scipy_linear_regression(X: List[float], y: List[float]) -> Tuple[float, float]:
    slope, intercept, _, _, _ = stats.linregress(X, y)
    return slope, intercept


# Define a function for linear regression using scikit-learn
def sklearn_linear_regression(X: List[float], y: List[float]) -> Tuple[float, float]:
    # Create a LinearRegression model
    model = LinearRegression()
    
    # Fit the model to the data
    model.fit(np.array(X).reshape(-1, 1), y)
    
    # Get the slope and intercept from the model
    slope = model.coef_[0]
    intercept = model.intercept_

    # return the slope and interface to whatever called this function
    return slope, intercept

################################
# Conditional Execution 
################################

# If the Python interpreter notices this file is running as the main module 
# Then, test the functions.
if __name__ == "__main__":
  
    # Create two data lists (must contain floating point numbers) 
    xlist: List[float] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    ylist: List[float] = [2.1, 3.2, 6.5, 8.3, 9.4, 12.8, 13.7, 16.4]
    
    # Test each of our functions
  
    print("==========================================")
    print("Using std_lib_statistics_linear_regression:")
    print("==========================================")
  
    m1, b1 = std_lib_statistics_linear_regression(xlist, ylist)
    print(f"Slope:     {m1}")
    print(f"Intercept: {b1}\n")
    
    print("==========================================")
    print("\nUsing numpy_linear_regression:")
    print("==========================================")
  
    m2, b2 = numpy_linear_regression(xlist, ylist)
    print(f"Slope:     {m2}")
    print(f"Intercept: {b2}\n")
  
    print("==========================================")
    print("\nUsing scipy_linear_regression:")
    print("==========================================")

    m3, b3 = scipy_linear_regression(xlist, ylist)
    print(f"Slope:     {m3}")
    print(f"Intercept: {b3}\n")

    print("==========================================")
    print("\nUsing sklearn_linear_regression:")
    print("==========================================")
    
    m4, b4 = sklearn_linear_regression(xlist, ylist)
    print(f"Slope:     {m4}")
    print(f"Intercept: {b4}\n")
      
    print("==========================================")
    print("\nUsing statsmodels_linear_regression:")
    print("==========================================")

    summary = statsmodels_linear_regression(xlist, ylist)
    print(summary)

    print("COMPLETE. ================================")

    
