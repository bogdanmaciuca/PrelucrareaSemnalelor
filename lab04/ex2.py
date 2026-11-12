import matplotlib.pyplot as plt
import numpy as np

f1 = 2.0 # < 5.0
f2 = 8.0 # > 5.0
fs = 10.0

t = np.linspace(0, 1, 1000)
ts = np.arange(0, 1.0+1/fs, 1/fs)

x1 = np.cos(2 * np.pi * f1 * t)
x2 = np.cos(2 * np.pi * f2 * t)

x1s = np.cos(2 * np.pi * f1 * ts)
x2s = np.cos(2 * np.pi * f2 * ts)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(t, x1)
ax.plot(t, x2)
ax.scatter(ts, x1s)
ax.scatter(ts, x2s)

plt.savefig('ex2.pdf')
plt.show()

