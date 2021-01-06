import numpy as np
import librosa
import soundfile as sf
from scipy.io import wavfile
from pesq import pesq


class MuLaw(object):
    def __init__(self, mu, int_type=np.int32, float_type=np.float32):
        self.mu = mu
        self.int_type = int_type
        self.float_type = float_type

    def transform(self, x):
        x = x.astype(self.float_type)
        y = np.sign(x) * np.log(1 + self.mu * np.abs(x)) / np.log(1 + self.mu)
        y = np.digitize(y, 2 * np.arange(self.mu) / self.mu - 1) - 1
        return y.astype(self.int_type)

    def itransform(self, y):
        y = y.astype(self.float_type)
        y = 2 * y / self.mu - 1
        x = np.sign(y) / self.mu * ((1 + self.mu) ** np.abs(y) - 1)
        return x.astype(self.float_type)


def get_audio(file, sample_rate):
    audio, _ = librosa.load(file, sr=sample_rate)
    return audio


def write_wav(audio, sample_rate, quantize):
    ml = MuLaw(quantize)
    audio_encoded = ml.transform(audio)
    audio_decoded = ml.itransform(audio)
    print(audio_encoded)
    print(audio_decoded)
    sf.write("mulaw.wav", audio_decoded, sample_rate)
    # return audio_encoded, audio_decoded


def calc_pesq(clean, noisy):
    rate, ref = wavfile.read(clean)
    rate, deg = wavfile.read(noisy)

    print(pesq(rate, ref, deg, "wb"))
    print(pesq(rate, ref, deg, "nb"))


if __name__ == "__main__":
    file = "./p257_270.wav"
    sample_rate = 16000
    quantize = 256
    audio = get_audio(file, sample_rate)
    audio /= np.abs(audio).max()
    audio = audio.astype(np.float32)
    write_wav(audio, sample_rate, quantize)

    clean = "./p257_270.wav"
    noisy = "./mulaw.wav"
    calc_pesq(clean, noisy)
