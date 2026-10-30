from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

fs = 100
Ts = 1 / fs

N = 20
n = np.arange(N)
t = n * Ts

t_cont = np.linspace(0, N * Ts, 2000)

freqs = [fs / 2, fs / 4, 0]

fig, axs = plt.subplots(3)
fig.suptitle("6.")
for ax, f in zip(axs, freqs):
    x = np.sin(-2 * np.pi * f * t)
    ax.plot(t_cont, np.sin(-2 * np.pi * f * t_cont), color="lightgray")
    ax.stem(t, x)
    ax.set_title(f"f={f:g}hz")
    fig.tight_layout()
    fig.savefig(out_dir / "6.pdf")

plt.show()
