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
from shiny.express import ui, input
from shinywidgets import render_plotly

# Import from our local utility 
# list everything we use
from util_lr import xlist, ylist, xlist2, ylist2, function_list

################################
# Define Global Variables
################################

# Create dictionary for dropdown options
function_options_dict = {name: name for name, _, _ in function_list}

# Create a function mapping with placeholder functions
def basic_linear_regression(xlist: List[float], ylist: List[float]) -> Tuple[float, float]:
    return statistics.linear_regression(xlist, ylist)

# Create a function mapping
function_mapping = {name: basic_linear_regression for name, _, _ in function_list}

    
##############################################
# Define a Reusable Function for Plotly Charts
##############################################

def get_chart(xlist: List[float], ylist: List[float], function_name: str) -> Figure:
    # Retrieve the function from the mapping
    if function_name in function_mapping:
        pass # chosen_function = function_mapping[function_name]
    else:
        raise ValueError(f"Function {function_name} not found in function mapping")

    # Fit linear regression model given our x and y lists using the chosen function
    slope, intercept = statistics.linear_regression(xlist, ylist)
    
    # Create a new plotly scatter chart from our data
    fig = px.scatter(
        x=xlist, 
        y=ylist, 
        labels={'x': 'X', 'y': 'Y'}, 
        title=f"{function_name} (Slope: {slope:.3f}, Intercept: {intercept:.3f})"
    )

    # Calculate the regression line using list comprehension
    regression_line = [slope * x + intercept for x in xlist]

    # Add the regression line to the chart
    fig.add_trace(px.line(x=xlist, y=regression_line).data[0])

    # Return the figure to whatever called this function
    return fig


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
    )
    
    ui.input_select(
        "f2",
        "Choose a function:",
        function_options_dict,
    )

# Use ui.h2() method to display a second-level heading (h2) 
# Pass in a string telling which method we used
ui.h2("Main Page")



################################
# Define & Render Plotly Charts
################################


with ui.layout_columns(col_widths=(4, 4)):

    @render_plotly
    def scatter_plot1() -> Figure:
        function_name = input.f1()
        fig1 = get_chart(xlist, ylist, function_name)

    @render_plotly
    def scatter_plot2() -> Figure:
        function_name = input.f2()
        fig2 = get_chart(xlist, ylist, function_name)

    @render_plotly
    def scatter_plot3() -> Figure:
        function_name = input.f1()
        fig1 = get_chart(xlist2, ylist2, function_name)

    @render_plotly
    def scatter_plot4() -> Figure:
        function_name = input.f2()
        fig2 = get_chart(xlist2, ylist2, function_name)
        
    
