from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

fs = 10_000
Ts = 1 / fs

A = 10
f = 5
phi = np.pi / 4

duration = 1
N = duration * fs
n = np.arange(N)
t = n * Ts

x_sin = A * np.sin(-2 * np.pi * f * t + phi)
x_cos = A * np.cos(-2 * np.pi * f * t + phi - np.pi / 2)

fig, axs = plt.subplots(2)
fig.suptitle("1.")
axs[0].plot(t, x_sin)
axs[0].set_title("sinus")
axs[1].plot(t, x_cos)
axs[1].set_title("cosinus")
fig.savefig(out_dir / "1.pdf")

plt.show()
