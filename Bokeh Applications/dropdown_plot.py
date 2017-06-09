from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource,Select
from bokeh.plotting import figure
from numpy.random import random,normal,lognormal


N=300
source=ColumnDataSource(data={'x':random(N),'y':random(N)})

plot=figure()
plot.circle('x','y',source=source)
menu=Select(options=['normal','uniform','lognormal'],value='uniform',title='Distribution')

#addding callback
def callback(attr,old,new):
    if menu.value == 'uniform':  f= random
    elif menu.value == 'normal': f= normal
   	else :                       f= lognormal
				source.data={'x':f(size=N),'y':f(size=N)}	

slider.on_change('value',callback)

layout=column(menu,plot)
curdoc().add_root(layout)
