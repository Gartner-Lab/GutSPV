"""
Reads simulation state from the given .npy file and writes a colored png image
with the same file body name.

Currently assumes three phases/cell types (see TODO below).
"""

import numpy as np
import sys, glob
import pathlib
# Assume SPV_plot is one up relative to this script:
sys.path.append( str(pathlib.Path(__file__).parent.resolve()) + "/../" )
from SPV_plot import *

# Width of the polygon edge line.
line_width = 0.5

# Colors to use for three phases.
colors = "#004D40", "#02E002", "#9E039F"      # dark green, light green, red/purple 
# colors = "#004D40", "#02E002", "#D81B60"    # dark green, light green, red
# colors = "#004D40", "#65FF65", "#D81B60"    # dark green, bright-light green, red
# colors = "#004D40", "#FFC107", "#D81B60"    # dark green, yellow, red
# colors = "#1E88E5", "#004D40", "#D81B60"    # blue, dark green, red
# colors = "#1E88E5", "#FFC107", "#D81B60"    # blue, yellow, red

# If input file given, use that. Otherwise just take all files in the folder.
if (len(sys.argv) == 2):
    input = [sys.argv[1]]
else:
    input = glob.glob('*.npy')

i = 0
for file in input:
    i = i+1
    print("Processing file %d / %d" %(i, len(input)))
    # Read domain dimensions (L), vertex positions (X) and list of cell types (c_types).
    L, X, c_types = np.load(file, allow_pickle=True)

    output = file.split(".")[0]     # output file name without .png extension
    plot_step( X, output, L, c_types, colors, plot_scatter=False, tri_save=False, \
               dir_name=".", line_width=line_width )
