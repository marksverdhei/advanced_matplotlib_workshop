from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi/2, 100)

X = 10 * np.outer(np.cos(u), np.sin(v))
Y = 10 * np.outer(np.sin(u), np.sin(v))
Z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
spheres = [ax.plot_surface(X, Y, Z,  rstride=4, cstride=4, cmap='spring'),
           ax.plot_surface(X, Y, -Z,  rstride=4, cstride=4, cmap='hot')]

def next_frame(i, spheres):
    spheres[0].remove()
    spheres[1].remove()
    theta = i/10
    Xi = np.cos(theta) * X - np.sin(theta) * Y
    Yi = np.sin(theta) * X + np.cos(theta) * Y

    Xj = np.cos(-theta) * X - np.sin(-theta) * Y
    Yj = np.sin(-theta) * X + np.cos(-theta) * Y

    spheres[0] = ax.plot_surface(Xi, Yi, Z, rstride=4, cstride=4, cmap='spring')
    spheres[1] = ax.plot_surface(Xj, Yj, -Z,  rstride=4, cstride=4, cmap='hot')


ani = FuncAnimation(fig, func=next_frame, fargs=(spheres,), interval=50, frames=200)

ani.save("spheres.gif", fps=30)
# plt.show()
