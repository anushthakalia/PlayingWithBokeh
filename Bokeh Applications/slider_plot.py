from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource,Slider
from bokeh.plotting import figure
from numpy.random import random


N=300
source=ColumnDataSource(data={'x':random(N),'y':random(N)})

plot=figure()
plot.circle('x','y',source=source)
slider=Slider(title='Number of points',start=100,end=1000,value=N,step=10)

#addding callback
def callback(attr,old,new):
    N=slider.value
    source.data={'x':random(N),'y':random(N)}

slider.on_change('value',callback)

layout=column(slider,plot)
curdoc().add_root(layout)
