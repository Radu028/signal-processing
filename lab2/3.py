from pathlib import Path

import numpy as np
import sounddevice as sd
from scipy.io import wavfile

fs = 44_100
Ts = 1 / fs
A = 1

f = 400
N = 1600
n = np.arange(N)
t = n * Ts
x_a = A * np.sin(-2 * np.pi * f * t)

f = 800
duration = 3
N = duration * fs
n = np.arange(N)
t = n * Ts
x_b = A * np.sin(-2 * np.pi * f * t)

f = 240
x_c = A * (2 * np.mod(f * t, 1) - 1)

f = 300
x_d = A * np.sign(np.sin(-2 * np.pi * f * t))

for x in [x_a, x_b, x_c, x_d]:
    sd.play(x, fs)
    sd.wait()

wav_path = Path(__file__).parent / "2b.wav"
wavfile.write(wav_path, fs, x_b.astype(np.float32))

rate, x_read = wavfile.read(wav_path)
print(rate, np.allclose(x_b, x_read))
