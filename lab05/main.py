import csv
import matplotlib.pyplot as plt
import numpy as np

x = np.genfromtxt('Train.csv', delimiter=',')[1:, 2]
N = len(x)

# a) 1/3600 = 0.0002777777777777778
Fs = 1/3600

# b) len(x) / 24 = 762 days

# c) Fs/1/3600/2 = 0.0001388888888888889 (Tmin=2h)

# d)
X = np.fft.fft(x)
X_mod = abs(X) / N
f = np.fft.fftfreq(N, d=3600)
f_half = f[:N//2]
X_half = X_mod[:N//2]
plt.figure()
plt.plot(f_half, X_half)
plt.savefig("d.pdf")
plt.show()

# e), f)
x0 = x - np.mean(x)
X = np.fft.fft(x0)
X[0] = 0
X_mod = abs(X) / N
X_half = X_mod[:N//2]
valid = f_half > 1e-8
f_valid = f_half[valid]
X_valid = X_half[valid]
top = np.argsort(X_valid)[-8:][::-1]
for i in top:
    fk = f_valid[i]
    perioada_ore = 1 / fk / 3600
    print(f"f = {fk:.3e} Hz, T = {perioada_ore:.2f} h")
plt.figure()
plt.yscale('log')
plt.plot(f_half, X_half)
plt.savefig("f.pdf")
plt.show()

# h)

