"""
Generic mesh initialization functions.

TODO: Turn this into a mesh representation for the SPV simulation.
"""

import numpy as np



def init_square_lattice( rows, cols, noise=0.0, rng_seed=1 ):
    """
    Constructs a lattice of square elements.
    """
    x = np.linspace(0, cols-1, cols)
    y = np.linspace(0, rows-1, rows)
    xv, yv = np.meshgrid(x, y)
    points = np.array([xv.flatten(), yv.flatten()]).T

    np.random.seed(rng_seed)
    noise = np.random.normal(0, noise, np.shape(points))
    points += noise

    return points
