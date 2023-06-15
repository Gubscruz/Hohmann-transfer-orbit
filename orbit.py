import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67430e-11  # Gravitational constant
M = 5.972e24     # Mass of the central body (Earth)

# Initial conditions
r0 = 150e6       # Initial distance from the central body (Earth)
v0 = 29.29e3     # Initial velocity

# Calculate orbital parameters
v_circular = np.sqrt(G * M / r0)
T = 2 * np.pi * r0 / v_circular
dt = T / 1000

# Generate time values
t = np.arange(0, T, dt)

# Calculate positions
x = r0 * np.cos(2 * np.pi * t / T)
y = r0 * np.sin(2 * np.pi * t / T)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-r0, r0)
ax.set_ylim(-r0, r0)
line, = ax.plot([], [], 'o-', lw=1)

# Animation update function
def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

# Create animation
animation = FuncAnimation(fig, update, frames=len(t), interval=10, blit=True)
plt.show()
