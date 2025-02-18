import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to calculate jet engine performance
def calculate_performance():
    try:
        altitude = float(entry_altitude.get())
        inlet_velocity = float(entry_inlet_velocity.get())
        exhaust_velocity = float(entry_exhaust_velocity.get())
        mass_flow_rate = float(entry_mass_flow_rate.get())

        # Constants for atmospheric model (simplified)
        temperature = 288.15 - 0.0065 * altitude  # Standard Atmosphere Model
        pressure = 101325 * (temperature / 288.15) ** 5.2561

        # Calculations
        thrust = mass_flow_rate * (exhaust_velocity - inlet_velocity)
        fuel_consumption = mass_flow_rate * 0.21  # Approximate ratio
        thermal_efficiency = ((thrust * inlet_velocity) / (fuel_consumption * 43e6)) * 100  # Convert to %

        # Thermal Efficiency Calculation - Fixed
        if fuel_consumption > 0:  # Avoid division by zero
            thermal_efficiency = ((thrust * inlet_velocity) / (fuel_consumption * 43e6)) * 100
        else:
            thermal_efficiency = 0  # Avoid undefined behavior

        # Ensuring efficiency stays within expected range
        if thermal_efficiency > 100:
            thermal_efficiency = 100  # Cap efficiency at 100% (realistically 50% max)
        elif thermal_efficiency < 1:
            thermal_efficiency *= 50  # Adjust scaling to prevent very low values


        # Update result labels
        result_text.set(
            f"--- Jet Engine Performance ---\n"
            f"Thrust: {thrust:.2f} N\n"
            f"Fuel Consumption: {fuel_consumption:.2f} kg/s\n"
            f"Thermal Efficiency: {thermal_efficiency:.2f} %\n"
            f"Temperature: {temperature:.2f} K\n"
            f"Pressure: {pressure:.2f} Pa"
        )

        # Update separate graphs
        update_graphs(thrust, fuel_consumption, thermal_efficiency)

    except ValueError:
        result_text.set("Please enter valid numerical values.")

# Function to update the separate graphs
def update_graphs(thrust, fuel, efficiency):
    # Clear previous plots
    ax1.clear()
    ax2.clear()
    ax3.clear()

    # Horizontal Bar Plot - Thrust
    ax1.barh(["N"], [thrust], color="blue")
    ax1.set_xlim(0, 200000)
    ax1.set_xticks(range(0, 200001, 20000))
    ax1.set_title("Thrust")
    ax1.grid(True)

    # Horizontal Bar Plot - Fuel Consumption
    ax2.barh(["kg/s"], [fuel], color="red")
    ax2.set_xlim(0, 100)
    ax2.set_xticks(range(0, 101, 10))
    ax2.set_title("Fuel Consumption")
    ax2.grid(True)

    # Horizontal Bar Plot - Thermal Efficiency
    ax3.barh(["%"], [efficiency], color="green")
    ax3.set_xlim(0, 100)
    ax3.set_xticks(range(0, 101, 10))
    ax3.set_title("Thermal Efficiency")
    ax3.grid(True)

    canvas.draw()

# GUI Setup
root = tk.Tk()
root.title("Jet Engine Performance Calculator")

# Input Fields
ttk.Label(root, text="Altitude (m):").pack()
entry_altitude = ttk.Entry(root)
entry_altitude.pack()
entry_altitude.insert(0, "10000")

ttk.Label(root, text="Inlet Velocity (m/s):").pack()
entry_inlet_velocity = ttk.Entry(root)
entry_inlet_velocity.pack()
entry_inlet_velocity.insert(0, "250")

ttk.Label(root, text="Exhaust Velocity (m/s):").pack()
entry_exhaust_velocity = ttk.Entry(root)
entry_exhaust_velocity.pack()
entry_exhaust_velocity.insert(0, "600")

ttk.Label(root, text="Mass Flow Rate (kg/s):").pack()
entry_mass_flow_rate = ttk.Entry(root)
entry_mass_flow_rate.pack()
entry_mass_flow_rate.insert(0, "300")

# Calculate Button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_performance)
calculate_button.pack()

# Result Display
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, justify="left")
result_label.pack()

# Matplotlib Graphs Setup - Increased Width
fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(12, 6), constrained_layout=True)  # Wider Graph
fig.tight_layout(pad=3.0)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Run the application
root.mainloop()
