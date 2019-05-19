import numpy
from scipy.io import wavfile
from numpy import fft
fs, data = wavfile.read('denisik.wav')
Te = 0.25
T = 40

a = data.T[0] #retrieve first channel
#put the information in a matrix, one row will contain the fourier coefficients of 0.25s of music.
#The whole matrix, which has 40 rows will contain information of 10s of the wav file.
X = numpy.array([fft(a[int(i*fs*Te):int((i+1)*fs*Te)]) for i in range(T)])
Z = fft.ifft(X.flatten())
Z = Z.astype(data.dtype)

wavfile.write('test3.wav',fs,Z)