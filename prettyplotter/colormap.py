""" 
Wrapper for creating a useful colormap
"""
import matplotlib as mpl
from matplotlib import cm
import numpy as np

def gray_sequentials(n: int) -> np.array:
    """Create a list of colors in a gray scale 
    sequential map for n samples"""
    start_points = cm.get_cmap('Greys', 5)
    interpolated_colors = np.zeros((n, 3))

    for i in range(3):
        interpolated_colors[:, i] = np.linspace(
            start_points(1)[i],
            start_points(2)[i],
            n
        )
    return interpolated_colors
