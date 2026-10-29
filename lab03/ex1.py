import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.animation import FuncAnimation

N = 8
F = np.zeros((N, N), dtype=complex)
for x in range(N):
    for y in range(N):
        F[x, y] = math.e ** (-2 * math.pi * 1j * x * y / N)

