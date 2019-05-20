import wave
import struct
import numpy as np
from math import exp, pi, sin
from scipy.io import wavfile as wav
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft
from scipy.io.wavfile import write

rate, ses = wav.read('str.wav')
length = len(ses)

sesData = [0 for x in range(length)]
j = 0
for i in ses:
    if j < length:
        sesData[j] = i[0]
        j += 1
ses_fft = fft(sesData)
#6118400
for i in range(80000, 6028400):
    ses_fft[i] = 0

plt.plot(np.real(ses_fft))
plt.show()


plt.plot(np.real(ses_fft))
plt.show()

ses_ifft = ifft(ses_fft)

plt.plot(np.real(ses_ifft))
plt.show()

write('test.wav', 44100, ses_ifft.astype(ses.dtype))

