# Autopilot PID Controller with Real-Time GUI

A real-time **PID controller simulation** for aircraft altitude stabilization, built with **Python, Tkinter, and Matplotlib**.

## Features
-  **Real-Time PID Tuning** – Adjust `Kp`, `Ki`, `Kd`, and Thrust **live** without restarting.
-  **Dynamic Visualization** – See how altitude and throttle input change over time.
-  **Smooth Updates** – The simulation auto-refreshes every 0.5s for instant feedback.
-  **Customizable Flight Physics** – Modify thrust, drag, and control response.

## Screenshot
(![Screenshot 2025-02-15 001542](https://github.com/user-attachments/assets/315a4eba-c17f-4739-8981-7eddc6af54e6)

---

## Installation & Running
1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/autopilot-pid-controller.git
   cd autopilot-pid-controller
2. **Install dependencies**:
   ```bash
   pip install matplotlib
3. **Run the simulation**:
   ```bash
   python main.py

## How it works
1. **PID Controler Adjustments**:
  -  **Kp (Proportional Gain): Controls how aggressively altitude is corrected.
  -  **Ki (Integral Gain): Fixes steady-state error over time.
  -  **Kd (Derivative Gain): Dampens overshoot and stabilizes responses.
  -  **Thrust Factor: Adjusts power available for altitude correction.
2. **Matplotlib Visualization**:
  -  **Top Graph: Altitude vs Time
  -  **Bottom Graph: Throttle (Control Input) vs Time
3. **Matplotlib Visualization**:
  -  **Move the sliders and watch the aircraft's altitude response change in real-time.
