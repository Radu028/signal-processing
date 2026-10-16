from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)


def x(t):
    return np.cos(520 * np.pi * t + np.pi / 3)


def y(t):
    return np.cos(280 * np.pi * t - np.pi / 3)


def z(t):
    return np.cos(120 * np.pi * t + np.pi / 3)


step = 0.0005
duration = 0.03

t = np.linspace(0, duration, round(duration / step) + 1)

fig, axs = plt.subplots(3)

axs[0].plot(t, x(t))
axs[1].plot(t, y(t))
axs[2].plot(t, z(t))

fig.savefig(out_dir / "1b.pdf")

hz = 200
freq = 1 / hz
n = np.linspace(0, duration, round(duration / freq) + 1)

fig.suptitle("1. c)")

axs[0].stem(n, x(n))
axs[1].stem(n, y(n))
axs[2].stem(n, z(n))

fig.savefig(out_dir / "1c.pdf")
plt.show()
