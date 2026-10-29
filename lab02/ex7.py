import numpy as np
import matplotlib.pyplot as plt

fs = 1000
f = 50
t = np.arange(0, 0.1, 1/fs)
x = np.sin(2 * np.pi * f * t)

t_dec1 = t[::4]
x_dec1 = x[::4]

t_dec2 = t[1::4]
x_dec2 = x[1::4]

fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# a)
axs[0].plot(t, x, color='lightgray', linestyle='--')
axs[0].plot(t_dec1, x_dec1, 'ro-')

# b)
axs[1].plot(t_dec1, x_dec1, 'ro-')
axs[1].plot(t_dec2, x_dec2, 'bs-')

plt.savefig("ex7.pdf")
plt.show()

