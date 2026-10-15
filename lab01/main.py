import matplotlib.pyplot as plt
import numpy as np

def ex1():
    def x(t): return np.cos(520 * np.pi * t + np.pi / 3)
    def y(t): return np.cos(280 * np.pi * t - np.pi / 3)
    def z(t): return np.cos(120 * np.pi * t + np.pi / 3)

    tc = np.arange(0, 0.03 + 0.0005, 0.0005)
    td = np.arange(0, 0.03 + 0.005, 0.005)

    fig, axs = plt.subplots(3, figsize=(8, 6))

    xc = x(tc)
    xd = x(td)
    axs[0].plot(tc, xc)
    axs[0].stem(td, xd)

    yc = y(tc)
    yd = y(td)
    axs[1].plot(tc, yc)
    axs[1].stem(td, yd)

    zc = z(tc)
    zd = z(td)
    axs[2].plot(tc, zc)
    axs[2].stem(td, zd)

    plt.savefig("ex1.pdf")
    plt.show()

def ex2():
    fig, axs = plt.subplots(4, figsize=(8, 8))

    # a)
    def fa(t): return np.sin(400 * np.pi * t)
    t = np.linspace(0, 1, 1600 * 4)
    ts = np.linspace(0, 1, 1600)
    axs[0].plot(t[:50 * 4], fa(t)[:50 * 4])
    axs[0].stem(ts[:50], fa(ts)[:50])

    # b)
    def fb(t): return np.sin(800 * np.pi * t)
    t = np.linspace(0, 3, 16000)
    axs[1].plot(t[:100], fb(t)[:100])

    # c)
    def fc(t): return 240*t - np.floor(240 * t)
    t = np.linspace(0, 1, 16000)
    axs[2].plot(t[:200], fc(t)[:200])

    # d)
    def fd(t): return np.sign(np.sin(300 * 2 * np.pi * t))
    t = np.linspace(0, 1, 16000)
    axs[3].plot(t[:200], fd(t)[:200])

    plt.savefig("ex2_abcd.pdf")
    plt.show()

    # e)
    img = np.random.rand(128, 128)
    plt.imshow(img)
    plt.savefig("ex2_e.pdf")
    plt.show()

    # f)
    img = np.zeros((128, 128), 'f')
    for x in range(128):
        for y in range(128):
            img[x, y] = np.sin(0.05 * x) * np.cos(0.05 * y)

    plt.imshow(img)
    plt.savefig("ex2_f.pdf")
    plt.show()


def ex3():
    pass

ex1()
ex2()

# === ex3 ===
# a) 1 / 2000 = 0.0005s = 0.5ms
# b) 2000 * 60 * 60 * 1/2 = 3600000B = 3.6MB

