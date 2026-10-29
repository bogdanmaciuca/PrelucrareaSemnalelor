import numpy as np
import matplotlib.pyplot as plt

A = 1
f = 3
fs = 1000
t = np.linspace(0, 1, fs)
phases = [0, np.pi/4, np.pi/2, np.pi]

plt.figure(figsize=(10, 4))
for phi in phases:
    x = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, x)

plt.savefig("ex2.pdf")
plt.show()

x = A * np.sin(2 * np.pi * f * t)
z = np.random.normal(0, 1, len(t))
snr_values = [0.1, 1, 10, 100]

fig, axs = plt.subplots(4, 1, figsize=(10, 8))
norm_x = np.linalg.norm(x)
norm_z = np.linalg.norm(z)

for i, snr in enumerate(snr_values):
    gamma = norm_x / (norm_z * np.sqrt(snr))
    x_noise = x + gamma * z

    axs[i].plot(t, x_noise, color='red', alpha=0.7)
    axs[i].plot(t, x, color='black')

axs[-1].set_xlabel('Timp [s]')
plt.savefig("ex2_noise.pdf")
plt.show()

