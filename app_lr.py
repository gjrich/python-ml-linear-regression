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
from shiny import render
from shiny.express import ui, input
from shinywidgets import render_plotly

# Import from our local utility 
# list everything we use in this file
from util_lr import xlist, ylist, xlist2, ylist2, function_list

################################
# Define Global Variables
################################

# Create dictionary for dropdown options
function_options_dict = {
    "none": "None", 
    "stat": "Std Lib Statistics",
    "numpy": "NumPy",
    "scipy": "SciPy",
    "statsmodels": "Statsmodels",
    "sklearn": "Scikit-Learn",
    "huber": "Scikit-Learn Huber",
    "ransac": "Scikit-Learn RANSAC",
}

# Create a function mapping with placeholder functions
def basic_linear_regression(xlist: List[float], ylist: List[float]) -> Tuple[float, float]:
    return statistics.linear_regression(xlist, ylist)

# Create a function mapping
function_mapping = {name: basic_linear_regression for name, _, _ in function_list}


################################
# Define the PyShiny Express UI
################################

# Use the PyShiny ui.page_opts() method to set the title 
ui.page_opts(title="Linear Regression Plot")

with ui.sidebar(bg="#EEF2F8"):  
    "Sidebar" 

    ui.input_select(
        "f1",
        "Choose a function:",
        function_options_dict,
        selected="stat"
    )

    ui.input_select(
        "f2",
        "Choose a function:",
        function_options_dict,
         selected="huber"
    )

    

################################
# Define & Render Output
################################

with ui.layout_columns(col_widths=(6,6)):
    with ui.card():
        
        @render.text
        def descrip1():
            return f"{function_options_dict[input.f1()]}"
        
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
   
    with ui.card():
        
        @render.text
        def descrip2():
            return f"{function_options_dict[input.f1()]}"
         
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
  
    with ui.card():
        
        @render.text
        def descrip3():
            return f"{function_options_dict[input.f2()]}"
        
        @render_plotly
        def scatter_plot3() -> Figure:
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
   
    with ui.card():
        
        @render.text
        def descrip4():
            return f"{function_options_dict[input.f2()]}"
         
        @render_plotly
        def scatter_plot4() -> Figure:
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
                       
