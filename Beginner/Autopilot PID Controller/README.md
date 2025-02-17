# Rocket Flight PID Controller

## Overview

This project simulates a rocket's ascent using a PID (Proportional-Integral-Derivative) Controller to reach a target altitude. The controller adjusts thrust dynamically to stabilize at the desired setpoint, mimicking real-world rocket launches where engines cut off once the altitude goal is reached.

## Features:

PID Control for Altitude Stabilization

Real-time Visualization (Altitude, Thrust, and PID errors)

Turtle Graphics Simulation of the rocket

Graph Plotting with Matplotlib

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
![Screenshot 2025-02-17 025830](https://github.com/user-attachments/assets/c8f1d1a7-895a-4d71-a29b-390fe6a2aec1)
![Screenshot 2025-02-17 025847](https://github.com/user-attachments/assets/c2acd4ba-3c9b-45a8-937f-275ca78684f4)

Thrust Graph: Displays the force applied over time.

PID Error Graph: Breaks down the Proportional, Integral, and Derivative errors in real time.
![Screenshot 2025-02-17 025853](https://github.com/user-attachments/assets/d59e7787-7d57-462f-ac7f-6177299851eb)

## Customization

Modify PID Gains (**, **, ``) in the script to see different flight behaviors.

Adjust Gravity and Thrust to simulate different planetary conditions.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

Inspired by aerospace engineering principles and real-world rocket stabilization methods.

Developed as an educational tool for understanding PID controllers in flight systems.
