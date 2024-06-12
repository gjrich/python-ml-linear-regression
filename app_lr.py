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

# Import from our local utility 
# list everything we use
from util_lr import xlist, ylist, xlist2, ylist2, functions

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
# Define & Render Plotly Charts
################################


@render_plotly
def scatter_plot1() -> Figure:
    ''' Define a function that returns a Plotly Figure'''
  
    # Fit linear regression model given our x and y lists
    slope, intercept = statistics.linear_regression(xlist, ylist)
    
    # Create a new plotly scatter chart from our data
    fig = px.scatter(
        x=xlist, 
        y=ylist, 
        labels={'x': 'X', 'y': 'Y'}, 
        title=f"Dataset 1 (Slope: {slope:.3f}, Intercept: {intercept:.3f})")

    # Calculate the regression line using list comprehension
    # Return mx+b for each x in the x list
    regression_line = [slope * x + intercept for x in xlist]

    # Create a plotly line using px.line() constructor method.
    # Use the figure's add_trace() method
    # Pass in the new line we created to add it to the chart
    fig.add_trace(px.line(x=xlist, y=regression_line).data[0])

    # Return the Figure object to whatever calls this function
    return fig

@render_plotly
def scatter_plot2() -> Figure:
    ''' Define a function that returns a Plotly Figure'''

    # Fit linear regression model given our x and y lists
    slope, intercept = statistics.linear_regression(xlist, ylist)
    
    # Create a new plotly scatter chart from our data
    fig = px.scatter(
        x=xlist2, 
        y=ylist2, 
        labels={'x': 'X', 'y': 'Y'}, 
        title=f"Dataset 2 (Slope: {slope:.3f}, Intercept: {intercept:.3f})")

    # Calculate the regression line using list comprehension
    # Return mx+b for each x in the x list
    regression_line = [slope * x + intercept for x in xlist2]

    # Create a plotly line using px.line() constructor method.
    # Use the figure's add_trace() method
    # Pass in the new line we created to add it to the chart
    fig.add_trace(px.line(x=xlist2, y=regression_line).data[0])

    # Return the Figure object to whatever calls this function
    return fig
