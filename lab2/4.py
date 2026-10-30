from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

fs = 10_000
Ts = 1 / fs

duration = 1
N = duration * fs
n = np.arange(N)
t = n * Ts

f_sin = 200
f_saw = 20

x_sin = np.sin(-2 * np.pi * f_sin * t)
x_saw = 2 * np.mod(f_saw * t, 1) - 1
x_sum = x_sin + x_saw

fig, axs = plt.subplots(3)
fig.suptitle("4.")
axs[0].plot(t, x_sin)
axs[0].set_title("sin")
axs[1].plot(t, x_saw)
axs[1].set_title("saw")
axs[2].plot(t, x_sum)
axs[2].set_title("sum")
fig.tight_layout()
fig.savefig(out_dir / "4.pdf")

plt.show()
