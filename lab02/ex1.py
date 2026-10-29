from matplotlib import pyplot as plt
import numpy as np

A = 1
f = 440
T = 3
rate = 44100

tc = np.linspace(0, T, rate)

fig, axs = plt.subplots(2)
# sin
s = A * np.sin(f * tc)
axs[0].plot(tc[:1000], s[:1000])
# cos
s = A * np.cos(f * tc - np.pi / 2)
axs[1].plot(tc[:1000], s[:1000])

plt.savefig("ex1.pdf")
plt.show()

