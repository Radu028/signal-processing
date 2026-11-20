from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

x = np.genfromtxt(
    Path(__file__).parent / "Train.csv", delimiter=",", skip_header=1, usecols=2
)
N = len(x)
fs = 1 / 3600

# d)
X = np.abs(np.fft.fft(x) / N)[: N // 2]
f = fs * np.arange(N // 2) / N

fig, ax = plt.subplots()
ax.plot(f, X)
fig.savefig(out_dir / "1d.pdf")

# e)
print("media:", x.mean())
xc = x - x.mean()
X = np.abs(np.fft.fft(xc) / N)[: N // 2]

# f)
for i in np.argsort(X)[::-1][:4]:
    print(f"{f[i]} Hz, perioada {1 / f[i] / 3600} ore")

# g)
start = 1056
fig, ax = plt.subplots()
ax.plot(x[start : start + 30 * 24])
fig.savefig(out_dir / "1g.pdf")

# i)
X_full = np.fft.fft(x)
f_full = np.fft.fftfreq(N, d=3600)
X_full[np.abs(f_full) > 1 / (6 * 3600)] = 0
x_filt = np.fft.ifft(X_full).real

fig, ax = plt.subplots()
ax.plot(x[start : start + 30 * 24])
ax.plot(x_filt[start : start + 30 * 24])
fig.savefig(out_dir / "1i.pdf")

plt.show()
