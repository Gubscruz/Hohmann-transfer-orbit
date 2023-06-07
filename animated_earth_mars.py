from earth_mars import *
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
mpl.use('pdf')

alpha = 44 # ideal position between the 180 degree alignment of the planets for the transfer
Earth = plt.Circle((0,0), radius= 1.0,fill=False,color='blue')
Mars = plt.Circle((0,0), radius= 1.52,fill=False,color='brown')

# creating and moving the planets
patch_E = plt.Circle((0.0, 0.0),radius=0.04,fill=True,color='blue')
patch_M = plt.Circle((0.0, 0.0),radius=0.03,fill=True,color='brown')
patch_H = plt.Circle((0.0, 0.0),radius=0.01,fill=True,color='red')


def init():
    ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
    # creating and moving the planets
    patch_E = plt.Circle((0.0, 0.0),radius=0.04,fill=True,color='blue')
    patch_M = plt.Circle((0.0, 0.0),radius=0.03,fill=True,color='brown')
    patch_H = plt.Circle((0.0, 0.0),radius=0.01,fill=True,color='red')
    
    patch_E.center = (0.0,0.0)
    ax.add_patch(patch_E)
    patch_M.center = (0.0,0.0)
    ax.add_patch(patch_M)
    patch_H.center = (0.0,0.0)
    ax.add_patch(patch_H)
    return patch_E,patch_M,patch_H

def animate(i):
#Earth
    x_E, y_E = patch_E.center
    x_E = np.cos((2*np.pi/365.2)*i)
    y_E = np.sin((2*np.pi/365.2)*i)
    patch_E.center = (x_E, y_E)
#Mars
    x_M, y_M = patch_M.center
    x_M = 1.52*np.cos((2*np.pi/686.98)*i+(np.pi*alpha/180.))
    y_M = 1.52*np.sin((2*np.pi/686.98)*i+(np.pi*alpha/180.))
    patch_M.center = (x_M,y_M)
#Hohmann
    delta = DeltaVs()
    Period = delta.transfer_time()*2
    x_H = 1.26 * (1 - 0.21**2) / (1 + 0.21 * np.cos((2*np.pi/Period)*i)) * np.cos((2*np.pi/Period)*i)
    y_H = 1.26 * (1 - 0.21**2) / (1 + 0.21 * np.cos((2*np.pi/Period)*i)) * np.sin((2*np.pi/Period)*i)
    patch_H.center = (x_H,y_H)
    return patch_E,patch_M,patch_H

Writer = animation.writers['pillow']
writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=1800)
plt.rc('font', family='serif', serif='Timer')
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('axes', labelsize=8)


fig, ax = plt.subplots(figsize=(10,8))
fig.subplots_adjust(left=.15, bottom=.16, right=.99, top=.97)
ax.plot(0,0,color='orange',marker='o',linestyle='',markersize=16,markerfacecolor='yellow',label='Sun')
ax.plot([],[],color='blue',linestyle='',marker='o',label='Earth')
ax.plot([],[],color='brown',linestyle='',marker='o',label='Mars')
ax.plot([],[],color='red',linestyle='',marker='o',label='spacecraft')
ax.add_patch(Earth)
ax.add_patch(Mars)
ax.set_xlabel('X [AU]',fontsize=12)
ax.set_ylabel('Y [AU]',fontsize=12)
ax.legend(loc='best',fontsize=12)
anim = animation.FuncAnimation(fig, animate,init_func=init,frames=260,interval=40,blit=True)
plt.axis('scaled') #Scale the plot in real time
anim.save('Hohmann.gif', writer='pillow')
plt.show()

