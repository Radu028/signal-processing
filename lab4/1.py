import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)


def dft(x):
    N = len(x)
    n = np.arange(N)
    F = np.exp(-2j * np.pi * np.outer(n, n) / N)
    return F @ x


def fft(x):
    N = len(x)
    if N == 1:
        return x
    even = fft(x[::2])
    odd = fft(x[1::2])
    w = np.exp(-2j * np.pi * np.arange(N // 2) / N) * odd
    return np.concatenate([even + w, even - w])


Ns = [128, 256, 512, 1024, 2048, 4096, 8192]
times = {"DFT": [], "FFT": [], "numpy.fft": []}

for N in Ns:
    x = np.random.rand(N)
    for name, func in [("DFT", dft), ("FFT", fft), ("numpy.fft", np.fft.fft)]:
        start = time.perf_counter()
        X = func(x)
        times[name].append(time.perf_counter() - start)
    print(N, np.allclose(dft(x), np.fft.fft(x)), np.allclose(fft(x), np.fft.fft(x)))

fig, ax = plt.subplots()
for name, t in times.items():
    ax.plot(Ns, t, "o-", label=name)
ax.set_yscale("log")
ax.legend()
fig.savefig(out_dir / "1.pdf")

plt.show()
