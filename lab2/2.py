from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

fs = 10_000
Ts = 1 / fs

f = 1

duration = 1
N = duration * fs
n = np.arange(N)
t = n * Ts

phis = [0, np.pi / 4, np.pi / 2, np.pi]

fig, ax = plt.subplots()
fig.suptitle("2.")
for phi in phis:
    x = np.sin(-2 * np.pi * f * t + phi)
    ax.plot(t, x, label=f"phi={phi / np.pi}pi")

ax.legend()
fig.savefig(out_dir / "2.pdf")

x = np.sin(-2 * np.pi * f * t)
z = np.random.normal(size=N)
snrs = [0.1, 1, 10, 100]

fig, axs = plt.subplots(len(snrs))
fig.suptitle("2.2")
for ax, snr in zip(axs, snrs):
    gamma = np.linalg.norm(x) / (np.sqrt(snr) * np.linalg.norm(z))
    ax.plot(t, x + gamma * z)
    ax.set_title(f"snr={snr}")
fig.tight_layout()
fig.savefig(out_dir / "2.2.pdf")

plt.show()
