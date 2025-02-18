# Calculates temperature and pressure at a given altitude using NASA's model
# Helps adjust jet engine calculations based on real-world conditions

import numpy as np

# Constants
R = 287.05 # Specific gas constant for dry air (J/kg.K)
g = 9.80665 # Gravity (m/s^2)
#----------

# Standard atmosphere layers (altitude in meters, temperature in Kelvin, pressure in Pascals)
layers = [
    (0, 288.15, 101325), # Sea level
    (11000, 216.65, 22632), # Troposphere end
    (20000, 216.65, 5474) # Stratosphere starts
]

def get_atmospheric_properties(altitude):
    """Returns temperature (K) and pressure (Pa) at a given altitude using NASA models."""
    for i in range(len(layers) - 1):
        h0, T0, P0 = layers[i]
        h1, T1, P1 = layers[i +1]
        
        if h0 <= altitude < h1:
            L = -0.0065 # Temperature lapse rate (K/m)
            T = T0 + L * (altitude - h0)
            P = P0 * (T / T0) ** (-g / (R * L))
            return T, P
        
    return layers[-1][1], layers[-1][2] # Return stratosphere values if above model limits