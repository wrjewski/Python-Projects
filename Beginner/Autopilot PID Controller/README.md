# Rocket Flight PID Controller

## Overview

This project simulates a rocket's ascent using a PID (Proportional-Integral-Derivative) Controller to reach a target altitude. The controller adjusts thrust dynamically to stabilize at the desired setpoint, mimicking real-world rocket launches where engines cut off once the altitude goal is reached.

## Features:

PID Control for Altitude Stabilization

Real-time Visualization (Altitude, Thrust, and PID errors)

Turtle Graphics Simulation of the rocket

Graph Plotting with Matplotlib

## Installation

Ensure you have Python installed. Then, install the necessary dependencies:

pip install numpy matplotlib

## Usage

Run the script using:

python PID_Video.py

## Input Parameters:

Starting Altitude: Initial height of the rocket.

Target Altitude: Desired altitude where the thrust cuts off.

Thrust Power: Determines the force applied to counteract gravity.

PID Tuning Values: Adjustments for smooth ascent control.

## Output:

A Graph Displaying Rocket Altitude, Thrust, and PID Errors

A Turtle Simulation of the Rocket's Motion

## Graphs Explained

Altitude Graph: Shows how the rocket ascends and stabilizes.

Thrust Graph: Displays the force applied over time.

PID Error Graph: Breaks down the Proportional, Integral, and Derivative errors in real time.

## Customization

Modify PID Gains (**, **, ``) in the script to see different flight behaviors.

Adjust Gravity and Thrust to simulate different planetary conditions.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

Inspired by aerospace engineering principles and real-world rocket stabilization methods.

Developed as an educational tool for understanding PID controllers in flight systems.
