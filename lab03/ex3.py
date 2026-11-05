import numpy as np
import matplotlib.pyplot as plt

N = 400
n = np.arange(N)
f_s = 200
t = np.arange(N) / f_s

A1, f1 = 1, 9
A2, f2 = 1.5, 5
A3, f3 = 0.5, 17

x = (A1 * np.sin(np.pi * 2 * f1 * t) +
    A2 * np.sin(np.pi * 2 * f2 * t) +
    A3 * np.sin(np.pi * 2 * f3 * t))

omegas = np.arange(1, 50)
magnitudes = []

for omega in omegas:
    X_omega = np.sum(x * np.exp(-2 * np.pi * 1j * n / f_s * omega))
    magnitudes.append(np.abs(X_omega))

fig, axs = plt.subplots(2, 1)
axs[0].plot(t, x)
axs[1].stem(omegas, magnitudes)
plt.savefig("ex3.pdf")
plt.show()

