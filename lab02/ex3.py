import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as signal
import sounddevice

fs = 44100
t = np.linspace(0, 2, 2 * fs)

sa = np.sin(2 * np.pi * 400 * t)
sb = np.sin(2 * np.pi * 800 * t)
sc = signal.sawtooth(2 * np.pi * 240 * t)
sd = signal.square(2 * np.pi * 300 * t)

sounddevice.play(sa, fs)
sounddevice.wait()

nume_fisier = 'ex3.wav'
wav.write(nume_fisier, fs, sa.astype(np.float32))

rr, rx = wav.read(nume_fisier)
print(f"rr={rr}Hz | len(xr)={len(rx)}")
