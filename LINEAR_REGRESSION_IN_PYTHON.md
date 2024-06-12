# Linear Regression In Python

It's common in data analytics to have a set of X, Y data points that we think might be linearly related. 
We can use the data to plot a simple straight line that "best fits" the data we have. 
By projecting the line, we can make predictions about additional values. 

The equation of a line is mx + b where m is the slope and b is where the line crosses the y-axis. 
That's all we need to draw our line: the slope and the intercept.
However, calculating that for a line that most closely matches our data would be a pain. 
Luckily Python makes it easy. 
The hardest part of our job is knowing which of the available approaches to use. 
And - what if anything should we do to clean the data first to generate the best and most accurate line through our data. 

Overall, our goal is a best fit line. Imagine we connected a thread from each data point to our "best fit" line. 
The general goal is to use as little thread as possible. 

## Fast and Easy Popular Options

These popular options all use the Least Mean Squared (LMS) calculation. 
LMS is a straightforward method for fitting a linear regression model. 
It calculates the line that best fits the data by minimizing the sum of the squared differences between the observed 
and predicted values. 

The goal is to minimize the threads - or as they are usually called, residuals.
We square each value so we don't have to worry about checking the direction of the distance - either postive or negative - before adding them all together.
It works pretty well. 
This method is computationally efficient and easy to implement. 
Unfortunately, if you get a high outlier, that distance to the line will be squared and it can significantly skew the results. 

Libraries like statistics (from the Python Standard Library) and numpy and scikit-learn offer options for LMS.
We can just call these functions or class methods and provide (pass in) our X and Y values.
They'll return the regression coefficients for the slope (as a floating point number) and the y-axis intercept (as a floating point number). 

| **Library**   | **In Standard Library** | **Method Used**                                      | **Example Function**                        |
|---------------|-------------------------|------------------------------------------------------|---------------------------------------------|
| `statistics`  | Yes                     | Least Mean Squared (LMS)                             | `statistics.linear_regression(x, y)`        |
| `statsmodels` | No                      | Least Mean Squared (LMS)                             | `sm.OLS(y, X)`                              |
| `numpy`       | No                      | Least Mean Squared (LMS)                             | `np.linalg.inv(X.T @ X) @ X.T @ y`          |
| `scikit-learn`| No                      | Least Mean Squared (LMS)                             | `LinearRegression().fit(X, y)`              |
| `scipy`       | No                      | Least Mean Squared (LMS)                             | `stats.linregress(X, y)`                    |


## Robust Regression Options (Better, but More Difficult, Longer)

If we want to avoid squaring those distances, we can use the Least Absolute Deviation (LAD) instead. 
Also known as Least Absolute Residual (LAR), this approach minimizes the combined sum of all the absolute differences between the observed and predicted values. 
We don't square it, so we have to calculate absolute values before we can sum everything up.
LAD gives equal weight to all data points, making it more robust to outliers (we don't further compound a large outliers by squaring their distance to the line). 
This method is often preferred in situations where the data may contain outliers or when the distribution of residuals (threads) is not normal.
It's more accurate, but harder to calculate, and can take longer. 

Here's some popular options that perform this more robust regression. 

## Libraries Supporting Robust Regression (Ordered by Popularity)

| **Library**      | **In Standard Library** | **Method Used**                                      | **Example Function**                                  |
|------------------|-------------------------|------------------------------------------------------|-------------------------------------------------------|
| `scikit-learn`   | No                      | Huber Regression                                     | `HuberRegressor().fit(X, y)`                          |
| `scikit-learn`   | No                      | RANSAC Regression                                    | `RANSACRegressor().fit(X, y)`                         |
| `statsmodels`    | No                      | Huber's T                                            | `RLM(y, X, M=sm.robust.norms.HuberT()).fit()`         |
| `scipy`          | No                      | Least Absolute Deviations (LMD)                      | `scipy.optimize.linprog`                              |
| `statsmodels`    | No                      | Quantile Regression (LMD)                            | `smf.quantreg('y ~ x', data)`                         |
| `numpy`          | No                      | Custom Least Absolute Deviations (LMD)               | `scipy.optimize.minimize`                             |


## Options Using a Different Approach

If we want to find the best fit line, we don't have to use least means squared - or even least absolute deviation. 
Instead we can try to optimize (minimize) the overall distance to the "best-fit" line. 
For that we can use the Gradient Descent algorithm. 
Gradient Descent iteratively adjusts the regression coefficients (slope and intercept) to get the steepest descent of the minimization function until it converges on a minimum.
Given the popularity of deep learning, it's  nice to see how these popular technologies can be used to gain similar insights. 

| **Library**   | **In Standard Library** | **Method Used**                                     | **Example Function**                      |
|---------------|-------------------------|-----------------------------------------------------|-------------------------------------------|
| `torch`       | No                      | Gradient Descent (used in deep learning contexts)  | `torch.optim.SGD` or `torch.nn.Linear`    |
| `tensorflow`  | No                      | Gradient Descent (used in deep learning contexts)  | `tf.keras.optimizers.SGD`                 |
| `jax`         | No                      | Gradient Descent (or other methods)                | `jax.numpy.linalg.solve`                  |


