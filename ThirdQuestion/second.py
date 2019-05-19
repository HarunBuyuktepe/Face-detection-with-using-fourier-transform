import wave
import struct
import numpy as np
from math import exp, pi,sin

ses=wave.open('sine24.wav', mode='rb')
print(wave.Wave_read.getsampwidth(ses))#Returns sample width in bytes
print(wave.Wave_read.getframerate(ses))#Returns sampling frequency.
print(wave.Wave_read.getnframes(ses))#Returns number of audio frames.
print(wave.Wave_read.getparams(ses))#Returns a namedtuple() (nchannels, sampwidth, framerate, nframes, comptype, compname), equivalent to output of the get*() methods.



if __name__ == '__main__':
    # http://stackoverflow.com/questions/3637350/how-to-write-stereo-wav-files-in-python
    # http://www.sonicspot.com/guide/wavefiles.html
    freq = 440.0
    data_size = 40000
    fname = "sine24.wav"
    frate = 11025.0
    amp = 64000.0
    nchannels = 1
    sampwidth = 2
    framerate = int(frate)
    nframes = data_size
    comptype = "NONE"
    compname = "not compressed"
    data = [sin(2 * pi * freq * (x / frate))
            for x in range(data_size)]
    wav_file = wave.open(fname, 'w')
    wav_file.setparams(
        (nchannels, sampwidth, framerate, nframes, comptype, compname))
    for v in data:
        wav_file.writeframes(struct.pack('h', int(v * amp / 2)))
    wav_file.close()

    print(wave.Wave_read.getsampwidth(wav_file))  # Returns sample width in bytes
    print(wave.Wave_read.getframerate(wav_file))  # Returns sampling frequency.
    print(wave.Wave_read.getnframes(wav_file))  # Returns number of audio frames.
    print(wave.Wave_read.getparams(
        wav_file))  # Returns a namedtuple() (nchannels, sampwidth, framerate, nframes, comptype, compname), equivalent to output of the get*() methods.
    data_size = 40000
    fname = "sine24.wav"
    frate = 11025.0
    wav_file = wave.open(fname, 'r')
    data = wav_file.readframes(data_size)
    wav_file.close()
    data = struct.unpack('{n}h'.format(n=data_size), data)
    data = np.array(data)

    w = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(w))
    print(freqs.min(), freqs.max())

    c=len(freqs)
    for i in range(c):
        if freqs[i]<0:
            freqs[i]*=-1
        print(freqs[i])

    print(freqs.min(), freqs.max())
    # (-0.5, 0.499975)

    # Find the peak in the coefficients
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * frate)
    print(freq_in_hertz)