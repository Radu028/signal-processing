from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

out_dir = Path(__file__).parent / "figs"
out_dir.mkdir(exist_ok=True)

fs, x = wavfile.read(Path(__file__).parent / "vocale.wav")
N = len(x)

L = N // 100
hop = L // 2
starts = np.arange(0, N - L + 1, hop)
groups = x[starts[:, None] + np.arange(L)]

S = np.abs(np.fft.fft(groups, axis=1))[:, : L // 2].T

fig, ax = plt.subplots()
ax.imshow(np.log10(S + 1), origin="lower", aspect="auto")
fig.savefig(out_dir / "6.pdf")

plt.show()
