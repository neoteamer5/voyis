import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================================
# Configuration
# ==========================================
acceleration = 0.625
initial_height = 20.0

# Vehicle 2 constant closing speed
y2_speed = 5.0

# Intersection
t_intersect = 8.0
y_intersect = 40.0

# Animation time: 0 to 10 seconds
x = np.linspace(0, 10, 300)

# ==========================================
# Vehicle 1: accelerate, then constant speed
# ==========================================
y1_ending_speed = acceleration * t_intersect
y1_ending_height = (
    initial_height
    + 0.5 * acceleration * t_intersect**2
)

y1 = np.where(
    x <= t_intersect,
    initial_height + 0.5 * acceleration * x**2,
    y1_ending_height
    + y1_ending_speed * (x - t_intersect)
)

# ==========================================
# Vehicle 2: constant closing speed
# ==========================================
y2 = y2_speed * x

# ==========================================
# Plot setup
# ==========================================
fig, ax = plt.subplots(figsize=(11, 7))

ax.set_xlim(0, 10)
ax.set_ylim(0, 60)
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Height")
ax.set_title(
    "Vehicle Motion: Acceleration, Intersection and Distance"
)
ax.grid(True, alpha=0.4)

# Animated curves
line1, = ax.plot(
    [], [], color="blue", linewidth=2,
    label="Vehicle 1: Accelerate, then cruise"
)

line2, = ax.plot(
    [], [], color="green", linewidth=2,
    label="Vehicle 2: constant closing speed"
)

# Moving vehicle markers
point1, = ax.plot([], [], "bo", markersize=8)
point2, = ax.plot([], [], "go", markersize=8)

# Fixed intersection marker
ax.plot(
    t_intersect, y_intersect,
    marker="*", color="red", markersize=17,
    label="Intersection (8s, 40m)", zorder=10
)

ax.annotate(
    "Intersection (8s, 40m)",
    xy=(t_intersect, y_intersect),
    xytext=(5.7, 48),
    fontsize=10,
    color="red",
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="red")
)

# Dynamic safty margin
distance_line, = ax.plot(
    [], [], "r--", linewidth=2,
    label="safty margin"
)

# Live information labels
time_label = ax.text(
    0.02, 0.96, "",
    transform=ax.transAxes,
    fontsize=11, va="top"
)

distance_label = ax.text(
    0.02, 0.90, "",
    transform=ax.transAxes,
    fontsize=11, color="red",
    fontweight="bold", va="top"
)

speed_label = ax.text(
    0.02, 0.84, "",
    transform=ax.transAxes,
    fontsize=10, va="top"
)

acceleration_label = ax.text(
    0.02, 0.78, "",
    transform=ax.transAxes,
    fontsize=10, color="blue",
    fontweight="bold", va="top"
)

ax.legend(loc="upper right", fontsize=9)

# ==========================================
# Animation update
# ==========================================
def update(i):
    t = x[i]

    # Current heights
    h1 = y1[i]
    h2 = y2[i]

    # safty margin between vehicles
    distance = abs(h1 - h2)

    # Vehicle 1 speed and acceleration
    if t < t_intersect:
        v1 = acceleration * t
        a1 = acceleration
        phase = "Accelerating"
    else:
        v1 = y1_ending_speed
        a1 = 0.0
        phase = "constant speed"

    # Update animated curves
    line1.set_data(x[:i + 1], y1[:i + 1])
    line2.set_data(x[:i + 1], y2[:i + 1])

    # Update vehicle markers
    point1.set_data([t], [h1])
    point2.set_data([t], [h2])

    # Update distance indicator
    distance_line.set_data([t, t], [h1, h2])

    # Update live labels
    time_label.set_text(f"Time = {t:.2f} s")

    distance_label.set_text(
        f"safty margin = |y1 - y2| = {distance:.3f}"
    )

    speed_label.set_text(
        f"Vehicle 1: {phase}, speed = {v1:.3f} m/s"
    )

    acceleration_label.set_text(
        f"Vehicle 1 acceleration = {a1:.3f} m/s²"
    )

    return (
        line1, line2, point1, point2,
        distance_line, time_label,
        distance_label, speed_label,
        acceleration_label
    )

# ==========================================
# Run animation
# ==========================================
ani = FuncAnimation(
    fig,
    update,
    frames=len(x),
    interval=1000 / 30,
    blit=True,
    repeat=False
)

plt.tight_layout()
plt.show()
