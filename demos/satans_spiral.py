import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(1)

spiral, = ax.plot(0, 0, color="r")
spiral2, = ax.plot(0, 0, color="k")
ax.set_aspect(1)

plt.xlim(-1.25,1.25)
plt.ylim(-1.25,1.25)

plt.grid(linestyle='--')

plt.title('Animations in matplotlib', fontsize=8)

def animation(i):
    theta = np.arange(max(0, i*2.1-420), i, 2.1)
    r = np.linspace(0, 1, theta.shape[0])
    x1 = r*np.cos(theta)
    x2 = r*np.sin(theta)
    spiral.set_data(x1, x2)
    spiral2.set_data(-x1, x2)

ani = FuncAnimation(fig, func=animation, interval=1, frames=380)
ani.save("satans_spiral5.gif", fps=60)

plt.show()
