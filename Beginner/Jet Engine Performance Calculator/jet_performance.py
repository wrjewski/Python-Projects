# Uses NASA's atmosphere model to get pressure and temperature at altitude
# Computes thrust, fuel consumption, and efficiency based on input parameters
# Provides a simple command-line interface for user input

import numpy as np
from nasa_atmosphere import get_atmospheric_properties

# Engine constants (simplified)
SPECIFIC_FUEL_CONSUMPTION = 0.6 # kg/s per kN of thrust
EFFICIENCY_FACTOR = 0.8 # Estimated engine efficiency
#------------------------------

def calculate_thrust(mass_flow_rate, velocity_exit, velocity_inlet):
    """Calculates jet engine thrust using mass flow rate and velocity change"""
    return mass_flow_rate * (velocity_exit - velocity_inlet)

def calculate_fuel_consumption(thrust):
    """Estimates fuel consumption based on thrust output"""
    return (thrust / 1000) * SPECIFIC_FUEL_CONSUMPTION # kg/s

def calculate_efficiency(velocity_exit, velocity_inlet):
    """Estimates thermal efficiency using kinetic energy difference"""
    ideal_efficiency = (1 - (velocity_inlet / velocity_exit)**2) * 100
    real_efficiency = ideal_efficiency * 0.85
    return round(real_efficiency, 2)

# CLI user input
altitude = float(input("Enter altitude (m): "))
velocity_inlet = float(input("Enter inlet velocity (m/s): "))
velocity_exit = float(input("Enter exhaust velocity (m/s): "))
mass_flow_rate = float(input("Enter mass flow rate (kg/s): "))

# Get atmospheric properties
temperature, pressure = get_atmospheric_properties(altitude)

# Calculate performance
thrust = calculate_thrust(mass_flow_rate, velocity_exit, velocity_inlet)
fuel_consumption = calculate_fuel_consumption(thrust)
efficiency = calculate_efficiency(velocity_exit, velocity_inlet)

# Display results
print("\n--- Jet Engine Performance ---")
print(f"Thrust Generated: {thrust:.2f} N")
print(f"Fuel Consumption: {fuel_consumption:.2f} kg/s")
print(f"Thermal Efficiency: {efficiency:.2f} %")
print(f"Atmospheric Temperature: {temperature:.2f} K")
print(f"Atmospheric Pressure: {pressure:.2f} Pa")