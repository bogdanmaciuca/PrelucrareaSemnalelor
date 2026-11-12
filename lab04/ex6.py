import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

fs, x = wavfile.read("vocals.wav")

x = x.astype(float)
N = len(x)

L = int(0.01 * N)
H = L // 2

cols = []
for start in range(0, N - L + 1, H):
    grup = x[start : start + L]
    spectru = np.abs(np.fft.rfft(grup))
    cols.append(spectru)

mat = np.column_stack(cols)
spec_db = 20 * np.log10(mat + 1e-12)
plt.figure(figsize=(10, 5))
plt.imshow(
    spec_db,
    aspect="auto",
    origin="lower",
    extent=[0, N / fs, 0, fs / 2],
)
plt.colorbar(label="Amplitude")
plt.xlabel("Time")
plt.ylabel("Freq")
plt.title("Spectrogram")
plt.tight_layout()
plt.savefig("ex6.pdf")
plt.show()

