import numpy as np
import matplotlib.pyplot as plt

fs = 20
t = np.arange(0, 1, 1/fs)

x_a = np.sin(2 * np.pi * (fs / 2) * t)
x_b = np.sin(2 * np.pi * (fs / 4) * t)
x_c = np.sin(2 * np.pi * 0 * t)

fig, axs = plt.subplots(3, 1)

axs[0].stem(t, x_a)

axs[1].stem(t, x_b)

axs[2].stem(t, x_c)

plt.savefig("ex6.pdf")
plt.show()

