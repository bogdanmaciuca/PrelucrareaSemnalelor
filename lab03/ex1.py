import math
import numpy as np
import matplotlib.pyplot as plt

# For loops
N = 8
F = np.zeros((N, N), dtype=complex)
for x in range(N):
    for y in range(N):
        F[x, y] = math.e ** (-2 * math.pi * 1j * x * y / N)

print("(For loops): np.conj(F) @ F == 8I_8 ->", np.allclose(np.conj(F) @ F, 8 * np.eye(8)))

# Numpy
F = np.exp(-2 * np.pi * 1j * np.arange(N) * np.arange(N)[:, None] / N)
print("(Numpy): np.conj(F) @ F == 8I_8 ->", np.allclose(np.conj(F) @ F, 8 * np.eye(8)))

fig, axs = plt.subplots(8, 1, figsize=(8, 12))
for i in range(8):
    axs[i].stem(np.arange(N), np.real(F[i]))
    axs[i].stem(np.arange(N), np.imag(F[i]), 'r')

plt.savefig("ex1.pdf")
plt.show()

