import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# PID Controller Class
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, measured_value, dt):
        """ Calculate PID control output """
        error = setpoint - measured_value
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else 0
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

        # Limit throttle range
        output = max(min(output, 5000), -5000)

        self.prev_error = error
        return output

# Function to update the PID simulation in real-time
def update_simulation():
    kp = kp_slider.get()
    ki = ki_slider.get()
    kd = kd_slider.get()
    thrust_factor = thrust_slider.get()

    pid = PIDController(kp, ki, kd)
    target_altitude = 1000
    sim_time = 10
    dt = 0.1
    time_steps = np.arange(0, sim_time, dt)
    altitude = 0
    altitudes = []
    control_inputs = []

    for t in time_steps:
        control_input = pid.compute(target_altitude, altitude, dt) * thrust_factor  # Adjust thrust
        thrust = control_input * dt
        drag = 0.1 * altitude  # Simulated air resistance
        altitude += (thrust - drag) * dt  # Apply physics
        altitudes.append(altitude)
        control_inputs.append(control_input)

    # Clear previous plots
    ax1.clear()
    ax2.clear()

    # Plot altitude response
    ax1.plot(time_steps, altitudes, label="Altitude")
    ax1.axhline(y=target_altitude, color='r', linestyle='--', label="Target Altitude")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Altitude (m)")
    ax1.legend()
    ax1.grid()

    # Plot control input (throttle)
    ax2.plot(time_steps, control_inputs, label="Control Input", color='g')
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Throttle")
    ax2.legend()
    ax2.grid()

    canvas.draw()

    # Schedule the next update
    root.after(500, update_simulation)  # Updates every 500ms (0.5s)

# Create the GUI window
root = tk.Tk()
root.title("PID Autopilot Tuning - Real-Time")

# Create figure and subplot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Create sliders
kp_slider = tk.Scale(root, from_=0.1, to=10.0, resolution=0.1, orient="horizontal", label="Kp")
kp_slider.set(3.5)
kp_slider.pack()

ki_slider = tk.Scale(root, from_=0.0, to=2.0, resolution=0.1, orient="horizontal", label="Ki")
ki_slider.set(0.2)
ki_slider.pack()

kd_slider = tk.Scale(root, from_=0.0, to=2.0, resolution=0.1, orient="horizontal", label="Kd")
kd_slider.set(0.8)
kd_slider.pack()

thrust_slider = tk.Scale(root, from_=0.1, to=2.0, resolution=0.1, orient="horizontal", label="Thrust Factor")
thrust_slider.set(1.0)
thrust_slider.pack()

# Start real-time updates
update_simulation()

# Run the Tkinter main loop
root.mainloop()
