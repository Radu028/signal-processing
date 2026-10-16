from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

fs = 100_000
Ts = 1 / fs

f = 400
N = 1600
n = np.arange(N)
t = n * Ts
s = np.sin(-2 * np.pi * f * t)

fig, axs = plt.subplots()
fig.suptitle("2. a)")
axs.plot(t, s)

fig.savefig(out_dir / "2a.pdf")

f = 800
duration = 3
N = duration * fs
n = np.arange(N)
t = n * Ts
s = np.sin(-2 * np.pi * f * t)

fig, axs = plt.subplots()
fig.suptitle("2. b)")
axs.plot(t, s)
axs.set_xlim([0, 0.01])
fig.savefig(out_dir / "2b.pdf")

f = 240
duration = 1
N = duration * fs
n = np.arange(N)
t = n * Ts
x = np.mod(f * t, 1)

fig, axs = plt.subplots()
fig.suptitle("2. c)")
axs.plot(t, x)
axs.set_xlim([0, 0.02])
fig.savefig(out_dir / "2c.pdf")

f = 300
duration = 1
N = duration * fs
n = np.arange(N)
t = n * Ts
x = np.sign(np.sin(-2 * np.pi * f * t))

fig, ax = plt.subplots()
fig.suptitle("2. d)")
ax.plot(t, x)
ax.set_xlim([0, 0.02])
fig.savefig(out_dir / "2d.pdf")

I = np.random.rand(128, 128)

fig, ax = plt.subplots()
fig.suptitle("2. e)")
ax.imshow(I)
fig.savefig(out_dir / "2e.pdf")

I = np.zeros((128, 128))
I[32:96, 32:96] = 1

fig, ax = plt.subplots()
fig.suptitle("2. f)")
ax.imshow(I)
fig.savefig(out_dir / "2f.pdf")
plt.show()
