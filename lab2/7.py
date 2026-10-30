from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

fs = 1000
Ts = 1 / fs

f = 50
duration = 0.1
N = round(duration * fs)
n = np.arange(N)
t = n * Ts
x = np.sin(-2 * np.pi * f * t)

x_a = x[::4]
t_a = t[::4]
x_b = x[1::4]
t_b = t[1::4]

fig, axs = plt.subplots(3)
fig.suptitle("7.")
axs[0].plot(t, x)
axs[0].set_title("original")
axs[1].plot(t, x, color="lightgray")
axs[1].plot(t_a, x_a)
axs[1].set_title("decimal de la primul element")
axs[2].plot(t, x, color="lightgray")
axs[2].plot(t_b, x_b)
axs[2].set_title("decimal de la al doilea element")
fig.tight_layout()
fig.savefig(out_dir / "7.pdf")

plt.show()
