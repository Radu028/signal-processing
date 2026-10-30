import numpy as np
import sounddevice as sd

fs = 44_100
Ts = 1 / fs
A = 1

duration = 1
N = round(duration * fs)
n = np.arange(N)
t = n * Ts

f1 = 440
f2 = 880

x1 = A * np.sin(-2 * np.pi * f1 * t)
x2 = A * np.sin(-2 * np.pi * f2 * t)
x = np.concatenate([x1, x2])

sd.play(x, fs)
sd.wait()

# desi amplitudinea e aceeasi al doilea e mai inalt
