import matplotlib.pyplot as plt
import numpy as np

f1 = 2.0 # < 5.0, < 9.0
f2 = 8.0 # > 5.0, < 9.0
fs1 = 10.0
fs2 = 18.0

t = np.linspace(0, 1, 1000)
ts1 = np.arange(0, 1.0+1/fs1, 1/fs1)
ts2 = np.arange(0, 1.0+1/fs2, 1/fs2)

x1 = np.cos(2 * np.pi * f1 * t)
x2 = np.cos(2 * np.pi * f2 * t)

x1s1 = np.cos(2 * np.pi * f1 * ts1)
x2s1 = np.cos(2 * np.pi * f2 * ts1)
x1s2 = np.cos(2 * np.pi * f1 * ts2)
x2s2 = np.cos(2 * np.pi * f2 * ts2)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(t, x1)
ax.plot(t, x2)
ax.scatter(ts1, x1s1, color="red")
ax.scatter(ts1, x2s1, color="red")
ax.scatter(ts2, x1s2, color="blue")
ax.scatter(ts2, x2s2, color="blue")

plt.savefig('ex3.pdf')
plt.show()


