import matplotlib.pyplot as plt
import numpy as np

f = 3
f_s = 200
N = f_s * 2
t = np.arange(N) / f_s

x = np.sin(2 * np.pi * f * t)

omegas = [1, 2, f, 7]

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs = axs.ravel()
for i, omega in enumerate(omegas):
    axs[i].set_title(f"w = {omega}Hz")
    axs[i].set_aspect('equal')
    axs[i].grid(True)
    y = x * np.exp(-2 * np.pi * 1j * omega * t)
    d = np.abs(y)
    axs[i].scatter(y.real, y.imag, c=d, s=20)
    axs[i].plot(y.real, y.imag)

plt.savefig("ex2.pdf")
plt.show()



y = x * np.exp(-2 * np.pi * 1j * f * t)
plt.ion()
fig_anim, ax_anim = plt.subplots(figsize=(6, 6))

(line_anim,) = ax_anim.plot([], [], color="tab:blue", alpha=0.5)
(point_anim,) = ax_anim.plot([], [], "ro", markersize=8)
(line_origin,) = ax_anim.plot([], [], color="red", linestyle="-")
ax_anim.grid(True)
ax_anim.set_aspect('equal')
ax_anim.set_xlim(-1.5, 1.5)
ax_anim.set_ylim(-1.5, 1.5)

for i in range(1, N, 2):
    line_anim.set_data(y[:i].real, y[:i].imag)
    point_anim.set_data([y[i].real], [y[i].imag])
    line_origin.set_data([0, y[i].real], [0, y[i].imag])
    plt.draw()
    plt.pause(0.01)

plt.ioff()
