from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

N = 8

n = np.arange(N)
omega = np.arange(N)
M = np.outer(omega, n)

F = np.exp(-2j * np.pi * M / N)

fig, axs = plt.subplots(N, figsize=(6.4, 10))
fig.suptitle("1.")
for ax, w, row in zip(axs, omega, F):
    ax.plot(n, row.real, label="real")
    ax.plot(n, row.imag, label="imaginar")
    ax.set_ylabel(f"omega={w}")
axs[0].legend()
fig.tight_layout()
fig.savefig(out_dir / "1.pdf")

FH = F.conj().T
print(np.allclose(FH @ F, N * np.eye(N)))
plt.show()
