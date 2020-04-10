import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib.animation import FuncAnimation

fig = plt.figure()
# Vi må bruke nøkkelordargumentet projection for å lage et tredimensjonalt kordinatsystem
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("x", fontsize=20)
ax.set_ylabel("y", fontsize=20)
ax.set_zlabel("z", fontsize=20)
ax = plt.axes(projection="3d")
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-2, 9)


def dots():
    # Vi lager 3 arrays med helt tilfeldige kordinater
    # og plotter det som punkter i kordinatsystemet
    X = np.random.random(1000)
    Y = np.random.random(1000)
    Z = np.random.random(1000)
    ax.scatter(X, Y, Z, c=Z+X+Y, cmap="coolwarm")


def surface():
    # Siden vi lager en kvadratisk overflate, trenger vi bare en array til å begynne med
    a = np.linspace(-420, 69, 11)
    X, Y = np.meshgrid(a, a)
    Z = h(X) + h(Y)
    Z *= np.sin(Z)
    return X, Y, Z


def bend():
    b = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(b, b)
    Z = f(X, g(Y))
    return X, Y, Z


def g(x):
    return -np.power(x, 4) + 2 * np.power(x, 3) + 2 * np.power(x, 2) - x

def h(x):
    return -4 * np.power(x, 3) + 6 * np.power(x, 2) + 4 * x - 1

def f(x, y):
    return g(x) + h(y)


def next_frame(frame_number):
    angle = frame_number/10
    surf[0].remove()
    surf2[0].remove()

    Xi = np.cos(angle) * X - np.sin(angle) * Y
    Yi = np.sin(angle) * X + np.cos(angle) * Y

    Yj = np.cos(angle) * Yi - np.sin(angle) * Z
    Zi = np.sin(angle) * Yi + np.cos(angle) * Z

    surf[0] = ax.plot_surface(Xi, Yj, Zi+(np.sin(angle)*5), cmap="coolwarm")
    surf2[0] = ax.plot_surface(-Xi, -Yj, -(Zi+(np.sin(angle)*5)), cmap="coolwarm_r")


X, Y, Z = bend()
Y = h(Y)
surf = [ax.plot_surface(X, Y, Z, cmap="coolwarm")]
surf2 = [ax.plot_surface(-X, -Y, -Z, cmap="coolwarm_r")]
ani = FuncAnimation(fig, next_frame, interval=20, frames=320)

# plt.show()
ani.save("../gifs/jesusfisk.gif", fps=60)
