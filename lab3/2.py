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

f = 3
x = np.sin(-2 * np.pi * f * t)

y = x * np.exp(-2j * np.pi * t)

k = 620

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle("2.")
axs[0].scatter(n, x, c=np.abs(x), s=2)
axs[0].plot([k, k], [0, x[k]], "r")
axs[0].plot(k, x[k], "ro")
axs[0].set_xlabel("Timp")
axs[0].set_ylabel("Amplitudine")
axs[1].scatter(y.real, y.imag, c=np.abs(y), s=2)
axs[1].plot([0, y[k].real], [0, y[k].imag], "r")
axs[1].plot(y[k].real, y[k].imag, "ro")
axs[1].set_aspect("equal")
axs[1].set_xlabel("Real")
axs[1].set_ylabel("Imaginar")
fig.tight_layout()
fig.savefig(out_dir / "2.1.pdf")

omegas = np.array([1, 2, f, 5])
Z = x * np.exp(-2j * np.pi * np.outer(omegas, t))

fig, axs = plt.subplots(2, 2, figsize=(8, 8))
fig.suptitle("2.2")
for ax, w, z in zip(axs.flat, omegas, Z):
    ax.scatter(z.real, z.imag, c=np.abs(z), s=2)
    ax.set_aspect("equal")
    ax.set_title(f"omega={w}Hz")
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginar")
fig.tight_layout()
fig.savefig(out_dir / "2.2.pdf")

fig, axs = plt.subplots(2, 2)
for i in range(0, N, 10):
    for ax, z in zip(axs.flat, Z):
        ax.clear()
        ax.scatter(z.real[: i + 1], z.imag[: i + 1], c=np.abs(z[: i + 1]), s=2)
        ax.plot(z[i].real, z[i].imag, "ro")
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_aspect("equal")
    plt.pause(0.01)

plt.show()
