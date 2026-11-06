from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

fs = 1000
Ts = 1 / fs

N = 1000
n = np.arange(N)
t = n * Ts

x = (
    np.cos(-2 * np.pi * 10 * t)
    + 2 * np.cos(-2 * np.pi * 30 * t)
    + 0.5 * np.cos(-2 * np.pi * 70 * t)
)

omega = np.arange(1, 101)
F = np.exp(-2j * np.pi * np.outer(omega, n) / N)
X = F @ x

fig, axs = plt.subplots(1, 2)
axs[0].plot(t, x)
axs[1].stem(omega, np.abs(X))
fig.savefig(out_dir / "3.pdf")

plt.show()
