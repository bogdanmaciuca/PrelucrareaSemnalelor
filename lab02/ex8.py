import matplotlib.pyplot as plt
import numpy as np

def pade(x):
    return (x - 7 * x ** 3 / 60) / (1 + x ** 2 / 20)

x = np.linspace(-np.pi/2, np.pi/2, 10000)

plt.plot(x, np.abs(x - np.sin(x)))
plt.plot(x, np.abs(pade(x) - np.sin(x)))
plt.yscale('log')
plt.show()

