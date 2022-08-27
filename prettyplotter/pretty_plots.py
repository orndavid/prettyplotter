""" 
API calls to various pretty plots
"""
from typing import Tuple
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from prettyplotter.colormap import gray_sequentials

def set_font(font: dict) -> None:
    mpl.rc('font', **font)

def default_font():
    set_font({
                 'family':'normal',
                 'size'  : 18
             })


def show():
    plt.show()


def xaxis_grid(ax: mpl.axes.Axes) -> None:
    """Set axes only for the x axis"""
    ax.xaxis.grid()
    ax.set_axisbelow(True)


def general_fig_ax(rows: int, cols: int, **kwargs):
    """rows : number of rows in a subfigure layout and cols is the 
    number of subfigures in a layout"""
    return plt.subplots(rows, cols, **kwargs)


def normalised_figure():
    return general_fig_ax(1, 1, figsize=(12, 10))


def remove_spines(ax: mpl.axes.Axes) -> None:
    """Removes the bounding box in a plot"""
    locations = ['top', 'right', 'bottom', 'left']
    for location in locations:
        ax.spines[location].set_visible(False)


def gray_bars(data :dict, **kwargs) -> Tuple[mpl.figure.Figure, mpl.axes.Axes]:
    """ 
    Gray bars create a sorted side-view bar graph with the keys (names)
    on the left side of the graph and the values shown. Pick the order 
    to be True for highest on top and False for highest on bottom. 

    Returns the figure handle and axes 

    **kwargs 
        'font' -> Dictionary to configure fonts using matplotlib.rc
        'order'-> True for ascending false for descending (default True)
        
    E.g. set specific font type
    """ 
    if 'font' in kwargs:
        set_font(kwargs['font'])
    else:
        default_font()
    if 'order' in kwargs:
        order = kwargs['order']
    else:
        order = True
    if 'max_height' in kwargs:
        max_height = kwargs['max_height']
    else:
        max_height = None


    if not isinstance(order, bool):
        raise ValueError(f'{__name__} - "order" must be boolean')
    
    no_values = len(data)
    names = []
    height_values = []
    for key in sorted(data, key=data.get, reverse=order):
        names.append(key)
        height_values.append(data[key])

    height_values = np.array(height_values)
    colormap = gray_sequentials(no_values)

    # Compute a pretty looking ratio between space and width of 
    # column
    width = 0.25
    padding = 0.05
    y_base_location = np.zeros((no_values, ))
    for i in range(1, no_values):
        y_base_location[i] = y_base_location[i-1] + (width+padding)

    fig, ax = normalised_figure()
    ax.barh(y_base_location, 
            height_values, 
            width,
            color=colormap, 
            tick_label=names)

    remove_spines(ax)
    xaxis_grid(ax)

    if max_height:
        ax.set_ylim([-1, max_height*(width+padding)+1])

    return fig, ax



