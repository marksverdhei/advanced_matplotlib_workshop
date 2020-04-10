from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_zlim(-100, 100)
# X, Y, Z = axes3d.get_test_data(0.40)
X, Y, Z = axes3d.get_test_data(0.05)

surface = [ax.plot_surface(X, Y, Z, cmap="viridis")]

def next_frame(i, surface):
    ax.set_title(r"$Z \cdot \sin( {0:.2f} )$".format(i/50))
    surface[0].remove()
    theta = i/50
    Xi = np.cos(theta) * X - np.sin(theta) * Y
    Yi = np.sin(theta) * X + np.cos(theta) * Y
    surface[0] = ax.plot_surface(Xi, Yi, Z*(np.sin(theta)+1), cmap="viridis")


ani = FuncAnimation(fig, func=next_frame, fargs=(surface,), interval=20, frames=315)

# ani.save("surface20.gif", fps=30)
plt.show()
