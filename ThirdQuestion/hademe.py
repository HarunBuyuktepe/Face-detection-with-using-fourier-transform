import wave

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft

n=100


ses = wave.open('sine24.wav', mode='rb')
Lx=100

omg = 2.0*np.pi/Lx

x=np.linspace(0, Lx, n)
y1 = 1.0*np.cos(5.0*omg*x)
y2 = 2.0 * np.sin(10.0 * omg * x)
y3 = 0.5 * np.sin(20.0 * omg * x)

y = y1 + y2 + y3

freqs = fftfreq(n)

mask = freqs > 0

fft_vals = fft(y)

fft_theo = 2.0 * np.abs(fft_vals/n)

plt.figure(1)
plt.subplot(211)
plt.title('Original Signal')
plt.plot(x, y, color='xkcd:salmon', label='orginal')
plt.legend()

plt.subplot(212)
plt.plot(freqs, fft_vals, label="raw fft values")
plt.title('Raw FFT values')

plt.show()
