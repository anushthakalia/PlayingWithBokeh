from bokeh.io import curdoc
from bokeh.layouts import column,widgetbox
from bokeh.models import ColumnDataSource,Button
from bokeh.plotting import figure
from numpy.random import random
import numpy as np

N=300
source=ColumnDataSource(data={'x':random(N),'y':random(N)})

plot=figure()
plot.circle('x','y',source=source)
# Create a Button with label 'Update Data'
button = Button(label='Update Data')


# Define an update callback with no arguments: update
def update():

    # Compute new y values: y
    y_new = np.sin(source.data['x']) + np.random.random(N)

    # Update the ColumnDataSource data dictionary
    source.data = {'x':source.data['x'],'y':y_new}

# Add the update callback to the button
button.on_click(update)

# Create layout and add to current document
layout = column(widgetbox(button), plot)
curdoc().add_root(layout)

# Other buttons are also available like checkbox group,toggle, radiogroup etc.