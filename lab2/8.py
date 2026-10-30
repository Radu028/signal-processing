from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

alpha = np.linspace(-np.pi / 2, np.pi / 2, 1000)

x_sin = np.sin(alpha)
x_taylor = alpha
x_pade = (alpha - 7 * alpha**3 / 60) / (1 + alpha**2 / 20)

err_taylor = np.abs(x_sin - x_taylor)
err_pade = np.abs(x_sin - x_pade)

fig, axs = plt.subplots(3)
fig.suptitle("8.")
axs[0].plot(alpha, x_sin, label="sin")
axs[0].plot(alpha, x_taylor, label="taylor")
axs[0].plot(alpha, x_pade, label="pade")
axs[0].set_title("functii")
axs[0].legend()
axs[1].plot(alpha, err_taylor, label="taylor")
axs[1].plot(alpha, err_pade, label="pade")
axs[1].set_title("eroare")
axs[1].legend()
axs[2].plot(alpha, err_taylor, label="taylor")
axs[2].plot(alpha, err_pade, label="pade")
axs[2].set_yscale("log")
axs[2].set_title("eroare log")
axs[2].legend()
fig.tight_layout()
fig.savefig(out_dir / "8.pdf")

plt.show()
