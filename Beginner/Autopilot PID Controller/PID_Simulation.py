import numpy as np
import matplotlib.pyplot as plt
import turtle 
import time

# GLOBAL PARAMETERS
TIMER = 0
TIME_STEP = 0.1  # Increased time step for smoother simulation
SETPOINT = 230  # Target altitude (m)
SIM_TIME = 500  # Total simulation time steps
INITIAL_X = 0
INITIAL_Y = 0  # Start at ground level
MASS = 1.0  # kg
MAX_THRUST = 25.0  # Max thrust in Newtons
g = -9.81  # Gravity (m/s²)
V_i = 0.0  # Initial velocity
Y_i = 0.0  # Initial height

# --- PID GAINS ---
KP = 0.8  # Increased for faster response
KI = 0.02  # Slightly increased for steady hold
KD = 0.15  # Increased to reduce oscillations
antiWindup = True  # Prevents integral windup

class Simulation:
    def __init__(self):
        self.rocket = Rocket()
        self.pid = PID(KP, KI, KD, SETPOINT)
        self.screen = turtle.Screen()
        self.screen.setup(800, 600)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.goto(15, SETPOINT)
        self.marker.color('red')
        self.sim = True
        self.timer = 0
        self.poses = np.array([])
        self.times = np.array([])
        self.kpe = np.array([])
        self.kde = np.array([])
        self.kie = np.array([])
        self.thrust = np.array([])

    def cycle(self):
        while self.sim:
            thrust = max(MASS * abs(g) + 2, self.pid.compute(self.rocket.get_y()))
            self.rocket.set_ddy(thrust)
            self.rocket.set_dy()
            self.rocket.set_y()
            time.sleep(TIME_STEP)
            self.timer += 1

            # Stop conditions
            if self.timer > SIM_TIME:
                print("SIM ENDED")
                self.sim = False
            elif self.rocket.get_y() > SETPOINT + 50:  # Soft boundary at the top
                print("OUT OF BOUNDS (High)")
                self.sim = False
            elif self.rocket.get_y() < -10:  # Soft boundary at the bottom
                print("OUT OF BOUNDS (Low)")
                self.sim = False

            # Store values for graphing
            self.poses = np.append(self.poses, self.rocket.get_y())
            self.times = np.append(self.times, self.timer)
            self.kpe = np.append(self.kpe, self.pid.get_kpe())
            self.kde = np.append(self.kde, self.pid.get_kde())
            self.kie = np.append(self.kie, self.pid.get_kie())
            self.thrust = np.append(self.thrust, thrust)

        # Generate graphs
        graph(self.times, self.poses, self.kpe, self.kde, self.kie, self.thrust)

def graph(x, height, kp_err, kd_err, ki_err, thrust):
    fig, axes = plt.subplots(3, figsize=(10, 6))  # 3 subplots
    fig.suptitle('Rocket Flight PID Performance')

    axes[0].plot(x, height, label="Rocket Altitude")
    axes[0].set_ylabel('Altitude (m)')
    axes[0].legend()
    axes[0].grid()

    axes[1].plot(x, thrust, label="Thrust", color="brown")
    axes[1].set_ylabel('Thrust (N)')
    axes[1].legend()
    axes[1].grid()

    axes[2].plot(x, kp_err, label="P Error", color="red")
    axes[2].plot(x, kd_err, label="D Error", color="orange")
    axes[2].plot(x, ki_err, label="I Error", color="pink")
    axes[2].set_ylabel('PID Errors')
    axes[2].legend()
    axes[2].grid()

    plt.xlabel("Time Steps")
    plt.show()

class Rocket:
    def __init__(self):
        self.Rocket = turtle.Turtle()
        self.Rocket.shape('square')
        self.Rocket.color('black')
        self.Rocket.penup()
        self.Rocket.goto(INITIAL_X, INITIAL_Y)
        self.Rocket.speed(0)

        # Physics
        self.ddy = 0
        self.dy = V_i
        self.y = INITIAL_Y

    def set_ddy(self, thrust):
        """Set acceleration (m/s²) including gravity compensation."""
        net_thrust = thrust - (MASS * abs(g))
        
        if abs(self.get_y() - SETPOINT) < 5:
            net_thrust *= 0.3
        self.ddy = g + (net_thrust / MASS)

    def get_ddy(self):
        return self.ddy

    def set_dy(self):
        """Calculate velocity based on acceleration."""
        self.dy += self.ddy * TIME_STEP

    def get_dy(self):
        return self.dy

    def set_y(self):
        """Move rocket in simulation and update position."""
        self.Rocket.sety(self.y + self.dy * TIME_STEP)

    def get_y(self):
        self.y = self.Rocket.ycor()
        return self.y

class PID:
    def __init__(self, KP, KI, KD, target):
        self.kp = KP
        self.ki = KI
        self.kd = KD
        self.setpoint = target
        self.error = 0
        self.integral_error = 0
        self.error_last = 0
        self.derivative_error = 0
        self.output = 0

    def compute(self, pos):
        """Compute thrust correction using PID control."""
        self.error = self.setpoint - pos
        self.derivative_error = (self.error - self.error_last) / TIME_STEP
        self.error_last = self.error

        # Compute PID output
        self.output = (
            self.kp * self.error
            + self.ki * self.integral_error
            + self.kd * self.derivative_error
        )
        
        # If close to setpoint, gradually decrease thrust
        if abs(self.error) < 5:
            self.output *+ 0.5
            
        self.output = min(max(self.output, 0), MAX_THRUST)
        
        return self.output

    def get_kpe(self):
        return self.kp * self.error

    def get_kde(self):
        return self.kd * self.derivative_error

    def get_kie(self):
        return self.ki * self.integral_error

def main():
    sim = Simulation()
    sim.cycle()

main()
