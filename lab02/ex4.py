import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

s_sin = np.sin(2 * np.pi * 5 * t)
s_saw = 0.5 * signal.sawtooth(2 * np.pi * 10 * t)
s_sum = s_sin + s_saw

fig, axs = plt.subplots(3, 1)

axs[0].plot(t, s_sin, color='blue')
axs[1].plot(t, s_saw, color='green')
axs[2].plot(t, s_sin, color='blue', alpha=0.5)
axs[2].plot(t, s_saw, color='green', alpha=0.5)
axs[2].plot(t, s_sum, color='purple')

plt.savefig("ex4.pdf")
plt.show()

