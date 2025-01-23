#
# Parameters for modeling the clustering of cells (phase 2) on a substrate (phase 1)
#
# Note: The parameters are divided into model dynamics and technical parameters. 
# To study the behavior of the model we most likely want to focus on dynamics. 
# Technical parameters have more to do with the implementation specifics of the 
# SPV model with less direct biological or experimental interpretation.
#

#
# Model dynamics
# 

domain_size = [60, 14]  # domain width, height
init_noise = 0.005      # amplitude of initial arrangement noise
rng_seed = 1            # random number generator seed
dt = 0.25              # simulation time step
tMax = 501             # simulation time end point

stripe_thickness = 4    # thickness of cells phase 
stripe_density = 0.5    # proportion of cells vs substrate within the stripe

v0 = [0.1, 1.3]         # motility of substrate, cells

# Interfacial energies as a 2x2 matrix:
# | substrate-substrate  substrate-cell |
# | cell-substrate       cell-cell      |
W = [0.0, 0.08], \
    [0.08, 0.0]

A0 = [0.9, 0.9] # target areas for cells, substrate
P0 = [3.812, 3.812] # Target perimeter

Dr = 50         # inverse of persistence timescale for motility
kappa_A = 0.4   # coefficient for deviation from target area in energy functional
kappa_P = 0.07  # same as above for perimeter
a = 0.25        # maximal radius to engage in repulsion
k = 2.5         # coefficient of repulsion
