import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# -----------------------------------------------------------------------------
# 1. Oscilloscope Screen Settings & Signal Parameters
# -----------------------------------------------------------------------------
width, height = 800, 500

t = np.linspace(0, 10, width)

# Signal parameters
freq = 0.5
amplitude = 1.8

true_phase1 = 0.0
true_phase2 = np.pi / 3       # 60 degrees

true_relative_phase = true_phase2 - true_phase1

# Clean 1D sine signals
sig1 = amplitude * np.sin(
    2 * np.pi * freq * t + true_phase1
)

sig2 = amplitude * np.sin(
    2 * np.pi * freq * t + true_phase2
)

# Add realistic noise
np.random.seed(42)

noise1 = np.random.normal(0, 0.05, width)
noise2 = np.random.normal(0, 0.05, width)

sig1_noisy = sig1 + noise1
sig2_noisy = sig2 + noise2


# -----------------------------------------------------------------------------
# 2. Render a Grayscale Oscilloscope Trace
# -----------------------------------------------------------------------------
def render_scope_trace(y_signal, height, thickness=1.5, blur=2.0):
    """
    Render a 1D waveform as a grayscale oscilloscope trace.
    """

    img = np.zeros((height, len(y_signal)))

    y_center = height // 2
    scale_y = height / 8.0

    y_pixels = y_center - (y_signal * scale_y)

    # Draw waveform
    for x_idx, y_val in enumerate(y_pixels):

        y_int = int(round(y_val))

        if 0 <= y_int < height:
            img[y_int, x_idx] = 1.0

    # Grayscale glow
    glow = gaussian_filter(img, sigma=blur) * 0.8
    core = gaussian_filter(img, sigma=0.5) * 1.2

    return np.clip(glow + core, 0, 1)


# Generate two grayscale traces
trace1 = render_scope_trace(
    sig1_noisy,
    height
)

trace2 = render_scope_trace(
    sig2_noisy,
    height
)


# -----------------------------------------------------------------------------
# 3. Combine the Two Traces into ONE Grayscale Image
# -----------------------------------------------------------------------------

# Both traces have the same grayscale intensity.
# Taking the maximum keeps both waveforms visible.
scope_img = np.maximum(trace1, trace2)

scope_img = np.clip(scope_img, 0, 1)


# -----------------------------------------------------------------------------
# 4. Phase Difference Processing
# -----------------------------------------------------------------------------

fft1 = np.fft.rfft(sig1_noisy)
fft2 = np.fft.rfft(sig2_noisy)

# Find dominant frequency
peak_bin = np.argmax(
    np.abs(fft1[1:])
) + 1

# Extract phase
phase1_meas = np.angle(
    fft1[peak_bin]
)

phase2_meas = np.angle(
    fft2[peak_bin]
)

# Relative phase
measured_rel_phase = phase2_meas - phase1_meas

# Wrap to [-pi, pi]
measured_rel_phase = np.arctan2(
    np.sin(measured_rel_phase),
    np.cos(measured_rel_phase)
)


# -----------------------------------------------------------------------------
# 5. Display Grayscale Oscilloscope
# -----------------------------------------------------------------------------

fig, ax = plt.subplots(
    figsize=(10, 6),
    facecolor="black"
)

ax.set_facecolor("black")

# Display grayscale oscilloscope image
ax.imshow(
    scope_img,
    extent=[0, 10, -4, 4],
    aspect="auto",
    origin="upper",
    cmap="gray",
    vmin=0,
    vmax=1
)


# -----------------------------------------------------------------------------
# 6. Oscilloscope Grid
# -----------------------------------------------------------------------------

ax.set_xticks(
    np.linspace(0, 10, 11)
)

ax.set_yticks(
    np.linspace(-4, 4, 9)
)

ax.grid(
    True,
    linestyle="--",
    linewidth=0.8,
    alpha=0.4
)

# Center axes
ax.axhline(
    0,
    linewidth=1.0,
    alpha=0.5
)

ax.axvline(
    5,
    linewidth=1.0,
    alpha=0.5
)


# Remove normal axis labels
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.tick_params(length=0)


# -----------------------------------------------------------------------------
# 7. Oscilloscope UI
# -----------------------------------------------------------------------------

ax.text(
    0.1,
    3.6,
    "TRIG'D",
    color="white",
    fontweight="bold",
    fontsize=9,
    bbox=dict(
        boxstyle="square,pad=0.2",
        facecolor="black",
        edgecolor="white"
    )
)

ax.text(
    0.2,
    -3.6,
    " CH1 ",
    color="white",
    fontweight="bold",
    fontsize=10
)

ax.text(
    2.0,
    -3.6,
    " CH2 ",
    color="white",
    fontweight="bold",
    fontsize=10
)

ax.text(
    4.0,
    -3.6,
    " M  1.00ms ",
    color="white",
    fontsize=10
)


# -----------------------------------------------------------------------------
# 8. Measurement Readout
# -----------------------------------------------------------------------------

meas_text = (
    "--- MEASUREMENT READOUT ---\n"
    f"True ΔΦ : "
    f"{true_relative_phase:.4f} rad "
    f"({np.degrees(true_relative_phase):.1f}°)\n"
    f"Meas ΔΦ : "
    f"{measured_rel_phase:.4f} rad "
    f"({np.degrees(measured_rel_phase):.1f}°)"
)

ax.text(
    6.3,
    2.5,
    meas_text,
    color="white",
    fontfamily="monospace",
    fontsize=9,
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="black",
        edgecolor="white"
    )
)


plt.tight_layout()
plt.show()


# -----------------------------------------------------------------------------
# 9. Console Summary
# -----------------------------------------------------------------------------

print("=" * 55)
print("     GRAYSCALE OSCILLOSCOPE PHASE PROCESSING")
print("=" * 55)

print(
    f"Ground Truth Relative Phase : "
    f"{true_relative_phase:.4f} rad "
    f"({np.degrees(true_relative_phase):.2f}°)"
)

print(
    f"Measured FFT Phase          : "
    f"{measured_rel_phase:.4f} rad "
    f"({np.degrees(measured_rel_phase):.2f}°)"
)

print(
    f"Phase Error                 : "
    f"{np.degrees(measured_rel_phase - true_relative_phase):.4f}°"
)

print("=" * 55)