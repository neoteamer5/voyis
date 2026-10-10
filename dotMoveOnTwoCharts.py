
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Time from 0 to 10 seconds
x = np.linspace(0, 10, 300)

# Two functions
y1 = (x**2)*25/80 + 20
y2 = 5*x

fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 105)
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("y")
ax.set_title("Animated Functions: y = x² + 2 and y = x")
ax.grid(True)
ax.legend(["y = x² + 2", "y = x"])

line1, = ax.plot([], [], label="y = x² + 2")
line2, = ax.plot([], [], label="y = x")
point1, = ax.plot([], [], "o")
point2, = ax.plot([], [], "o")
time_label = ax.text(0.02, 0.94, "", transform=ax.transAxes)

ax.legend()

def update(i):
    line1.set_data(x[:i + 1], y1[:i + 1])
    line2.set_data(x[:i + 1], y2[:i + 1])

    point1.set_data([x[i]], [y1[i]])
    point2.set_data([x[i]], [y2[i]])

    time_label.set_text(f"Time = {x[i]:.2f} seconds")
    return line1, line2, point1, point2, time_label

ani = FuncAnimation(
    fig, update,
    frames=len(x),
    interval=1000 / 30,
    blit=True,
    repeat=False
)

plt.show()
