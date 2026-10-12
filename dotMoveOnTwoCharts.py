import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

# ==========================================
# Configuration
# ==========================================
acceleration = 0.625
initial_height = 20.0

# Vehicle 2 constant closing speed
y2_speed = 5.0

# tangent
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
    "Vehicle Motion: Acceleration, Tangent point and Distance"
)
ax.grid(True, alpha=0.4)

# Animated curves
line1, = ax.plot(
    [], [], color="blue", linewidth=2,
    label="Vehicle 1: Accelerate, then cruise"
)

# Green line with 50% transparency
line2, = ax.plot(
    [], [], color="green", linewidth=2, alpha=0.5,
    label="Vehicle 2: constant closing speed"
)

# Moving vehicle markers
point1, = ax.plot([], [], "bo", markersize=8)

# Hollow green marker for vehicle 2 (no facecolor)
point2, = ax.plot(
    [], [],
    marker="o",
    linestyle="",
    markersize=8,
    markerfacecolor="none",
    markeredgecolor="green",
    markeredgewidth=1.5,
    alpha=0.9  # edge slightly transparent
)

# Fixed tangent marker
ax.plot(
    t_intersect, y_intersect,
    marker="*", color="red", markersize=5,
    label="Tangent (8s, 40m)", zorder=10
)

ax.annotate(
    "Tangent (8s, 40m)",
    xy=(t_intersect, y_intersect),
    xytext=(5.7, 48),
    fontsize=10,
    color="red",
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="red")
)

# Dynamic safety margin
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

acceleration_label = ax.text(
    0.02, 0.84, "",
    transform=ax.transAxes,
    fontsize=10, color="blue",
    fontweight="bold", va="top"
)

speed_label = ax.text(
    0.02, 0.78, "",
    transform=ax.transAxes,
    fontsize=10, va="top"
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

    # safety margin between vehicles
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
        f"safty margin = |y1 - y2| = {distance:.3f} m"
    )

    speed_label.set_text(
        f"Vehicle 1: {phase}, speed = {v1:.3f} m/s\n"
        f"Vehicle 2: constant speed, speed = {y2_speed:.3f} m/s"
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
# Create animation (initial)
# ==========================================
ani = FuncAnimation(
    fig,
    update,
    frames=len(x),
    interval=1000 / 30,
    blit=True,
    repeat=False
)

# ==========================================
# Buttons: Pause/Resume and Restart
# ==========================================
paused = False  # Track paused state

# Pause button (toggle)
ax_pause = plt.axes([0.66, 0.02, 0.12, 0.05])
btn_pause = Button(ax_pause, "Pause")

def pause(event):
    global paused
    if not paused:
        # pause animation
        try:
            ani.event_source.stop()
        except Exception:
            pass
        btn_pause.label.set_text("Resume")
        paused = True
    else:
        try:
            ani.event_source.start()
        except Exception:
            pass
        btn_pause.label.set_text("Pause")
        paused = False

btn_pause.on_clicked(pause)

# Restart button
ax_restart = plt.axes([0.80, 0.02, 0.12, 0.05])
btn_restart = Button(ax_restart, "Restart")

def restart(event):
    """
    Ensure restart works even if the previous animation has completed.
    Approach: stop current animation timer (if any), clear artists, then
    recreate the FuncAnimation object and start it (or keep it paused if paused==True).
    Recreating avoids edge cases where the internal iterator/frame sequence
    is exhausted after the animation finishes.
    """
    global ani, paused

    # try to stop existing event source (if any)
    try:
        ani.event_source.stop()
    except Exception:
        pass

    # Clear current plot state (so initial frame is empty/clean)
    line1.set_data([], [])
    line2.set_data([], [])
    point1.set_data([], [])
    point2.set_data([], [])
    distance_line.set_data([], [])
    time_label.set_text("")
    distance_label.set_text("")
    speed_label.set_text("")
    acceleration_label.set_text("")

    # Recreate the FuncAnimation to ensure fresh frame iterator
    ani = FuncAnimation(
        fig,
        update,
        frames=len(x),
        interval=1000 / 30,
        blit=True,
        repeat=False
    )

    # If we should remain paused, stop the new event source and set button text accordingly
    if paused:
        try:
            ani.event_source.stop()
        except Exception:
            pass
        btn_pause.label.set_text("Resume")
    else:
        btn_pause.label.set_text("Pause")
        try:
            ani.event_source.start()
        except Exception:
            pass

    # Force a draw of the initial state so user sees the cleared plot immediately
    update(0)
    fig.canvas.draw_idle()

# When GUI (figure) is closed, print Vehicle 1 acceleration and
# number of seconds to accelerate, and save the figure.
def on_close(event):
    try:
        print(f"Vehicle 1 acceleration = {acceleration} m/s^2")
        print(f"Seconds to accelerate = {t_intersect} s")
        # save the current figure
        fig.savefig("VehicleMotion_1f2t.png", bbox_inches="tight")
        print("Saved figure to VehicleMotion_1f2t.png")
    except Exception as e:
        print("Error during on_close:", e)


# Connect the close event handler
fig.canvas.mpl_connect("close_event", on_close)

btn_restart.on_clicked(restart)

# leave 8% at bottom for widgets
## leave space for the buttons plt.show()
plt.show()
