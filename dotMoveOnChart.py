
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 10, 300)
y = np.sin(t)

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("y = sin(t)")
ax.set_title("Sine Wave Animation")
ax.grid(True)

line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], "ro")

def update(i):
    line.set_data(t[:i + 1], y[:i + 1])
    point.set_data([t[i]], [y[i]])
    return line, point

ani = FuncAnimation(
    fig, update,
    frames=len(t),
    interval=1000 / 30,
    blit=True,
    repeat=False
)

plt.show()
