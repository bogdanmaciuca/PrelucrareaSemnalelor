import matplotlib.pyplot as plt
import numpy as np
import time

def timer(fn, x, reps=5):
    fn(x) # Warmup

    t0 = time.perf_counter()
    for _ in range(reps):
        fn(x)
    return (time.perf_counter() - t0) / reps

def dft(x):
    return np.exp(-2 * np.pi * 1j * np.arange(N) * np.arange(N)[:, None] / N) @ x

def radix2(x):
    x = np.asarray(x, dtype=complex)
    N = x.size
    if N == 1:
        return x.copy()

    assert N & (N - 1) == 0

    even = radix2(x[0::2])
    odd = radix2(x[1::2])

    W = np.exp(-2j * np.pi * np.arange(N // 2) / N)
    t = W * odd
    return np.concatenate([even + t, even - t])

N_vals = [128, 256, 512, 1024, 2048, 4096]
rng = np.random.default_rng(1)

funcs = {
    "dft":    (dft,        3),
    "radix2": (radix2,     10),
    "np.fft": (np.fft.fft, 10),
}
times = { name: [] for name in funcs}

def print_table(N_vals, times):
    names = list(times.keys())

    wN   = max(len("N"), *(len(str(N)) for N in N_vals))
    wcol = max(len(n) for n in names) + 2

    header = f"{'N':>{wN}}  " + "  ".join(f"{n:>{wcol}}" for n in names)
    print(header)
    print("-" * len(header))

    for i, N in enumerate(N_vals):
        linie = f"{N:>{wN}}  " + "  ".join(
            f"{times[n][i]:>{wcol}.6f}" for n in names
        )
        print(linie)

for N in N_vals:
    x = rng.standard_normal(N) + 1j * rng.standard_normal(N)
    for name, (fn, reps) in funcs.items():
        times[name].append(timer(fn, x, reps=reps))

print_table(N_vals, times)

plt.figure()
for name in times:
    plt.loglog(N_vals, times[name], label=name)
plt.grid(True, which='both')
plt.legend()
plt.savefig('ex1.pdf')
plt.show()

