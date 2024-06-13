################################
# app.py
################################

################################
# Import Packages First
################################

# Python Standard Library Packages
import random
import statistics
from typing import List, Tuple, Callable

# External Packages (must be installed)
# Use requirements.txt
# List one package per line

# Plotly for interactive charts
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs._figure import Figure

# PyShiny packages
from shiny import render, reactive
from shiny.express import ui, input
from shinywidgets import render_plotly

# Local module import - use util_lr
# list all the top-level variables and functions we need in app.py
from util_lr import xlist, ylist, xlist2, ylist2, function_list, function_mapping, description_mapping, get_slope_and_intercept

################################
# Define Global Variables
################################

# Create dictionary for dropdown options
function_options_dict = {
    "stat": "Std Lib Statistics",
    "numpy": "NumPy",
    "scipy": "SciPy",
    "statsmodels": "Statsmodels",
    "sklearn": "Scikit-Learn",
    "huber": "Scikit-Learn Huber",
    "ransac": "Scikit-Learn RANSAC",
}

################################
# Define the PyShiny Express UI
################################

# Use the PyShiny ui.page_opts() method to set the title 
ui.page_opts(title="Why Do We Square Things in Linear Regression?")

with ui.sidebar(bg="#EEF2F8"):  
    "User Selections" 

    ui.input_select(
        "selected_first_method",
        "Method 1",
        function_options_dict,
        selected="stat"
    )

    ui.input_select(
        "selected_second_method",
        "Method 2:",
        function_options_dict,
         selected="huber"
    )

    ui.input_select(
        "selected_dataset",
        "Choose a dataset:",
        {"1":"Dataset 1",
        "2":"Dataset 2"},
         selected="1"
    )


################################
# Reactive calcs 
# Update automatically when inputs change
################################

# Reactive calculations for selected functions
@reactive.calc
def selected_function_1():
    return function_mapping[input.selected_first_method()]

@reactive.calc
def selected_function_2():
    return function_mapping[input.selected_second_method()]

@reactive.calc
def getXY():
    if input.selected_dataset() == "1":
        return xlist, ylist
    else:
        return xlist2, ylist2

################################
# Define & Render Output
################################

with ui.layout_columns(col_widths=(6,6)):
    
    with ui.card():
        
        @render.text
        def method1():
            return f"{function_options_dict[input.selected_first_method()]}"

        @render.text
        def descrip1():
            return f"{description_mapping[input.selected_first_method()]}"
 
        @render_plotly
        def scatter_plot1() -> Figure:
            ''' Define a function that returns a Plotly Figure'''

            method = input.selected_first_method()
            xvalues, yvalues = getXY()
            slope, intercept = get_slope_and_intercept(xvalues, yvalues, method)
            
            # Create a new plotly scatter chart from our data
            fig = px.scatter(
                x=xvalues, 
                y=yvalues, 
                labels={'x': 'X', 'y': 'Y'}, 
                title=f"Slope: {slope:.3f}, Intercept: {intercept:.3f}")
       
            # Calculate the regression line using list comprehension
            # Return mx+b for each x in the x list
            regression_line = [slope * x + intercept for x in xvalues]
        
            # Create a plotly line using px.line() constructor method.
            # Use the figure's add_trace() method
            # Pass in the new line we created to add it to the chart
            fig.add_trace(px.line(x=xvalues, y=regression_line).data[0])
        
            # Return the Figure object to whatever calls this function
            return fig
   

    with ui.card():
        
        @render.text
        def method2():
            return f"{function_options_dict[input.selected_second_method()]}"

        @render.text
        def descrip2():
            return f"{description_mapping[input.selected_second_method()]}"
        
        @render_plotly
        def scatter_plot3() -> Figure:
            ''' Define a function that returns a Plotly Figure'''
        
            method = input.selected_second_method()
            xvalues, yvalues = getXY()
            slope, intercept = get_slope_and_intercept(xvalues, yvalues, method)
            
            fig = px.scatter(
                x=xvalues, 
                y=yvalues, 
                labels={'x': 'X', 'y': 'Y'}, 
                title=f"Slope: {slope:.3f}, Intercept: {intercept:.3f}")
        
            regression_line = [slope * x + intercept for x in xvalues]
            fig.add_trace(px.line(x=xvalues, y=regression_line).data[0])
            return fig
   
