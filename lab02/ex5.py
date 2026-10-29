import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import scipy.signal as signal

fs = 44100
dur = 1.5
t = np.linspace(0, dur, int(fs * dur), endpoint=False)

f1 = 440
f2 = 880

s1 = 0.5 * np.sin(2 * np.pi * f1 * t)
s2 = 0.5 * np.sin(2 * np.pi * f2 * t)

concat = np.concatenate((s1, s2))

wav.write('ex5.wav', fs, concat.astype(np.float32))

sd.play(concat, fs)
sd.wait()


