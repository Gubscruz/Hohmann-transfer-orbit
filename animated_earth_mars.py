import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Constants
G = 6.67430e-11  # gravitational constant
M = 5.972e24  # mass of Earth
mu = G * M  # gravitational parameter
r1 = 6371e3  # radius of lower circular orbit (Earth's orbit)
r2 = 42164e3  # radius of higher circular orbit (Mars' orbit)

# Calculate semi-major axis of the transfer orbit
a = (r1 + r2) / 2

# Time array for one full orbit in the transfer ellipse
T = np.linspace(0, 2*np.pi, 300)

# Position function for an elliptical orbit with semi-major axis a and eccentricity e
def position(a, e, T):
    r = a * (1 - e**2) / (1 + e * np.cos(T))
    return r * np.cos(T), r * np.sin(T)

# Create plot
fig, ax = plt.subplots()
ax.set_xlim(-r2 - r1, r2 + r1)
ax.set_ylim(-r2 - r1, r2 + r1)
ax.set_aspect('equal')

# Add orbits to plot
earth_orbit = Circle((0, 0), r1, fill=False, color='b', linestyle='--')
mars_orbit = Circle((0, 0), r2, fill=False, color='r', linestyle='--')
ax.add_artist(earth_orbit)
ax.add_artist(mars_orbit)

# Add planets to plot
earth = Circle((r1, 0), r1/10, color='b')
mars = Circle((-r2, 0), r2/10, color='r')
ax.add_artist(earth)
ax.add_artist(mars)

# Plot spacecraft
spacecraft, = ax.plot([], [], 'go')

# Initialize function
def init():
    spacecraft.set_data([], [])
    return spacecraft,

# Eccentricity of the transfer orbit
e = 1 - 2 / ((r2 / r1) + 1)

# Update function
def update(i):
    x, y = position(a, e, T[i])
    spacecraft.set_data(x, y)
    return spacecraft,

# Create animation
ani = FuncAnimation(fig, update, frames=range(len(T)), init_func=init, blit=True)

plt.show()
