from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

a = np.linspace(-10, 10, 20)

X, Y = np.meshgrid(a, a)

def f(x, y):
    return np.sin(x) + np.sin(y)

Z = f(X, Y)

surface = [ax.plot_surface(X, Y, Z, cmap="gnuplot2")]

def next_frame(i, surface):

    surface[0].remove()
    theta = i/50
    Xi = np.cos(theta) * X - np.sin(theta) * Z
    Zi = np.sin(theta) * X + np.cos(theta) * Z

    Xj = np.cos(theta) * Xi - np.sin(theta) * Y
    Yi = np.sin(theta) * Xi + np.cos(theta) * Y
    surface[0] = ax.plot_surface(Xj, Yi, Zi, cmap="gnuplot2")


ani = FuncAnimation(fig, func=next_frame, fargs=(surface,), interval=50, frames=315)

# ani.save("kuleloype6.gif", fps=60)
plt.show()
