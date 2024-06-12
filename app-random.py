################################
# Import Packages First
################################

# Python Standard Library Packages
import random
import statistics
from typing import List, Tuple

# Plotly for interactive charts
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs._figure import Figure

# PyShiny packages
from shiny.express import ui  
from shinywidgets import render_plotly

################################
# Define Global Variables
################################

# Set some input variables 
# Include data type hints
given_num_points: int = 50
given_slope : float = 2.0
given_intercept : float = 12.0
given_noise_std : float = 1.0

################################
# Define Functions
################################

# Define a function to generate a set of x, y data points
# The parameters define the variable names used locally, inside this function
def generate_data_points(num_points: int, slope: float, intercept: float, noise_std: float) -> Tuple[List[float], List[float]]:
    '''Generate x, y data points with a specified linear relationship and noise.'''

    # Set the random seed for reproducibility
    random.seed(0)
    
    # Generate a list of random x values between 0 and 1
    x_list: List[float] = [random.random() for _ in range(num_points)]
    
    # Generate a list of noise values using a Gaussian distribution
    # The noise is centered around 0 with a standard deviation of noise_std
    noise_values: List[float] = [random.gauss(0, noise_std) for _ in range(num_points)]
    
    # Calculate the corresponding y values based on the linear equation y = mx + b + noise
    y_list: List[float] = [slope * x + intercept + noise for x, noise in zip(x_list, noise_values)]
    
    # Return the generated x and y values as a tuple to whatever calls this function
    return x_list, y_list

################################
# Define the PyShiny Express UI
################################

# Use the PyShiny ui.page_opts() method to set the title 
ui.page_opts(title="Linear Regression Plot")

# Use ui.h1() method to display a second-level heading (h2) 
# Pass in a string telling which method we used
ui.h2("Built with Statistics Package")

# Use ui.p() method to display a paragraph (p)
# Pass in an f-string (a formatted string)
# to combine text and with our input value
ui.p(f"Count of Points: {given_num_points}")


################################
# Define & Render Plotly Chart
################################


@render_plotly
def scatter_plot() -> Figure:
    ''' Define a function that returns a Plotly Figure'''
  
    # Call our function to generate our x list and y list of values
    xlist, ylist = generate_data_points(given_num_points, given_slope, given_intercept, given_noise_std)
    
    # Fit linear regression model given our x and y lists
    slope, intercept = statistics.linear_regression(xlist, ylist)
    
    # Create a new plotly scatter chart from our data
    fig = px.scatter(
        x=xlist, 
        y=ylist, 
        labels={'x': 'X', 'y': 'Y'}, 
        title=f"Linear Regression Demo (Slope: {slope:.3f}, Intercept: {intercept:.3f})")

    # Calculate the regression line using list comprehension
    # Return mx+b for each x in the x list
    regression_line = [slope * x + intercept for x in xlist]

    # Create a plotly line using px.line() constructor method.
    # Use the figure's add_trace() method
    # Pass in the new line we created to add it to the chart
    fig.add_trace(px.line(x=xlist, y=regression_line).data[0])

    # Return the Figure object to whatever calls this function
    return fig
