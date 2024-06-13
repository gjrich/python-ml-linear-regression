################################
# util_lr module - import into app.py
################################

################################
# Import Packages First
################################

# Python Standard Library Packages
import csv
import statistics
from typing import List, Tuple

# External Packages (must be installed)
# Use requirements.txt and list 
# One package per line

import numpy as np
from scipy import stats
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression, HuberRegressor, RANSACRegressor

################################
# Define Sample Data Sets
################################

# Data Set 1
# Two lists of floating point numbers, one for x and one for y
xlist: List[float] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
ylist: List[float] = [2.1, 3.2, 6.5, 8.3, 9.4, 12.8, 13.7, 16.4]

# Data Set 2
# Two lists of floating point numbers, one for x and one for y
xlist2: List[float] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
ylist2: List[float] = [2.1, 3.2, 6.5, 8.3, 9.4, 12.8, 13.7, 100.0] 


################################
# Define function_list
################################

def numpy_linear_regression(X: List[float], y: List[float]) -> Tuple[float, float]:
    ''' Use NumPy Linear Regression (LMS)'''
    X = np.array(X)
    y = np.array(y)
    X = np.vstack([np.ones(len(X)), X]).T  # Adds intercept term
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
    return theta[1], theta[0]  # Returns slope, intercept

def scipy_linear_regression(X: List[float], y: List[float]) -> Tuple[float, float]:
    ''' Use SciPy Linear Regression (LMS)'''
    slope, intercept, _, _, _ = stats.linregress(X, y)
    return slope, intercept

def statsmodels_linear_regression(X: List[float], y: List[float]) -> Tuple[float, float]:
    ''' Use Statsmodels Linear Regression (LMS)'''
    X = sm.add_constant(X)  # Adds intercept term
    model = sm.OLS(y, X).fit()
    slope, intercept = model.params[1], model.params[0]
    return slope, intercept

def sklearn_linear_regression(X: List[float], y: List[float]) -> Tuple[float, float]:
    ''' Use Scikit-Learn Linear Regression (LMS)'''
    model = LinearRegression()
    model.fit(np.array(X).reshape(-1, 1), y)
    return model.coef_[0], model.intercept_

def sklearn_huber_regression(X: List[float], y: List[float]) -> Tuple[float, float]:
    ''' Use Scikit-Learn Huber Regression (LAD)'''
    model = HuberRegressor().fit(np.array(X).reshape(-1, 1), y)
    return model.coef_[0], model.intercept_

def sklearn_ransac_regression(X: List[float], y: List[float]) -> Tuple[float, float]:
    ''' Use Scikit-Learn RANSAC Regression (LMS)'''
    model = RANSACRegressor().fit(np.array(X).reshape(-1, 1), y)
    return model.estimator_.coef_[0], model.estimator_.intercept_

def display_table(results: List[dict], decimal_points: int, dataset: str) -> None:
    '''Display results in a formatted table for a specific dataset'''
    print(f"\nResults for {dataset} dataset:")
    print("{:<25} {:<10} {:<12} {:<12}".format("Method", "Type", "Slope", "Intercept"))
    print("="*60)
    format_str = f"{{:<25}} {{:<10}} {{:<12.{decimal_points}f}} {{:<12.{decimal_points}f}}"
    for result in results:
        if result["Dataset"] == dataset:
            print(format_str.format(result["Method"], result["Type"], result["Slope"], result["Intercept"]))

def show_sm_summary(X: List[float], y: List[float]) -> None:
    '''Display detailed summary for Statsmodels Linear Regression'''
    X_with_const = sm.add_constant(X)
    sm_model = sm.OLS(y, X_with_const).fit()
    print(sm_model.summary())

################################
# Define A List of Test Tuples
################################

# List of functions, each a tuple with information

function_list = [
    ("Std Lib Statistics", statistics.linear_regression, "LMS"),
    ("NumPy", numpy_linear_regression, "LMS"),
    ("SciPy", scipy_linear_regression, "LMS"),
    ("Statsmodels", statsmodels_linear_regression, "LMS"),
    ("Scikit-Learn", sklearn_linear_regression, "LMS"),
    ("Scikit-Learn Huber", sklearn_huber_regression, "Robust"),
    ("Scikit-Learn RANSAC", sklearn_ransac_regression, "Robust")
]

# Dictionary (key-value pairs) of functions
# Map a short string to the actual function name

function_mapping = {
    "stat": statistics.linear_regression,
    "numpy": numpy_linear_regression,
    "scipy": scipy_linear_regression,
    "statsmodels": statsmodels_linear_regression,
    "sklearn": sklearn_linear_regression,
    "huber": sklearn_huber_regression,
    "ransac": sklearn_ransac_regression
}

################################
# Conditional Execution 
################################

if __name__ == "__main__":

    ################################
    # If we run this module as a script, then test our functions
    # Make sure these functions work correctly
    # before importing these functions into another module.
    ################################

    # Results list to store each result as a dictionary
    results = []

    # Run each function and store results for Data Set 1
    for name, func, method in function_list:
        slope, intercept = func(xlist, ylist)
        results.append({"Method": name, "Type": method, "Slope": slope, "Intercept": intercept, "Dataset": "1"})

    # Run each function and store results for Data Set 2
    for name, func, method in function_list:
        slope, intercept = func(xlist2, ylist2)
        results.append({"Method": name, "Type": method, "Slope": slope, "Intercept": intercept, "Dataset": "2"})

    # Write results to CSV file
    with open("linear_regression_results.csv", "w", newline="") as csvfile:
        fieldnames = ["Method", "Type", "Slope", "Intercept", "Dataset"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

    # Display the results as a table with 8 decimal points for slope and intercept
    display_table(results, 8, "1")
    display_table(results, 8, "2")

    # Additional detailed summary from Statsmodels 
    print("\nDetailed Summary for Statsmodels Linear Regression (Dataset 1):")
    show_sm_summary(xlist, ylist)

    print("\nDetailed Summary for Statsmodels Linear Regression (Dataset 2):")
    show_sm_summary(xlist2, ylist2)
