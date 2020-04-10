import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
radius = 0.1

x = 0

X = radius*np.cos(x)
Y = radius*np.sin(x)

fig, ax = plt.subplots(1)

line, = ax.plot(X, Y)
ax.set_aspect(1)

plt.xlim(-1,1)
plt.ylim(-1,1)

plt.grid()

plt.title("Enkel sirkel")

def next_frame(frame):
    x = np.arange(0, frame, 0.1)
    radius = np.linspace(0, 1, x.shape[0])
    X = radius*np.cos(x)
    Y = radius*np.sin(x)
    line.set_xdata(X)
    line.set_ydata(Y)

ani = FuncAnimation(fig, next_frame, interval=10)

plt.show()
