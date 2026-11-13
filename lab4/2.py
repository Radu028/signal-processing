from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

f = 3
fs = 5
n = np.arange(fs)
ts = n / fs

t = np.linspace(0, 1, 1000)

fig, axs = plt.subplots(4)
axs[0].plot(t, np.sin(2 * np.pi * f * t))
for ax, f_i in zip(axs[1:], [3, 8, 13]):
    ax.plot(t, np.sin(2 * np.pi * f_i * t))
    ax.plot(ts, np.sin(2 * np.pi * f_i * ts), "o")
fig.savefig(out_dir / "2.pdf")

plt.show()
