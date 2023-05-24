import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
mpl.use('pdf')

fig = plt.figure()
axis = plt.axes(xlim=(-0.5, 1), ylim=(-1.5, 1.5))
line, = axis.plot([], [], lw=2)

# Initialisation function: plot the background of each frame
# indicates witch objects are moving on each frame

def init():
    line.set_data([], [])
    return line,

# Animation function which updates figure data.  This is called sequentially

def animate(i):
    x = np.linspace(-1, 1, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)
anim.save('animation.gif', writer='pillow')