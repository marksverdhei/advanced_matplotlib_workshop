import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(1)

spiral, = ax.plot(0, 0, color="r")
# spiral2, = ax.plot(0, 0, color="k")
# spiral3, = ax.plot(0, 0, color="g")
# spiral4, = ax.plot(0, 0, color="y")
ax.set_aspect(1)

plt.xlim(-1.25,1.25)
plt.ylim(-1.25,1.25)

plt.grid(linestyle='--')

plt.title('Animations in matplotlib', fontsize=8)

def animation(i):

    # i = i % 700

    theta = np.arange(max(0, (1.69*i)-500), i, 1.69)
    r = np.linspace(0, 1, theta.shape[0])
    # r = np.arange(0, i, 0.01)
    x1 = r*np.cos(theta)
    x2 = r*np.sin(theta)
    spiral.set_data(x1, x2)
    # spiral2.set_data(-x1, x2)
    # spiral3.set_data(-x1, x2)
    # spiral4.set_data(x1, -x2)

ani = FuncAnimation(fig, func=animation, interval=1, frames=700)
ani.save("../gifs/spiral.gif", fps=60)
plt.show()
