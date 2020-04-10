import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot()
x_data = np.linspace(-10, 10, 100)
sinx = np.sin(x_data)
cosx = np.cos(x_data)
ax.set_xlim(-10, 10)
ax.set_ylim(2, -2)
line1, = plt.plot(x_data, sinx)
line2, = plt.plot(x_data, cosx)
def next_frame(frame_number):
    i = frame_number/10
    line1.set_ydata(np.sin(x_data*i))
    line2.set_ydata(np.cos(x_data/np.sqrt(i)))

ani = FuncAnimation(fig, func=next_frame, interval=50)

plt.show()
