import numpy as np
import matplotlib.pyplot as plt
import sklearn
import librosa
import librosa.display

# load file
file_path = '/Users/m/Desktop/recordings/separated/volumeup'
file_name = '0.wav'
file = file_path + '/' + file_name
y ,sample_rate = librosa.load(file)

# check sampling rate & the length
print('Sampling rate (Hz): %d' %sample_rate)
print('Audio length (seconds): %.2f' % (len(y) / sample_rate))

# # normalize from 0 to 1
# def normalize(x, axis=0):
#   return sklearn.preprocessing.minmax_scale(x, axis=axis)
# mfccs = librosa.feature.mfcc(y, sr=sr)
# mfccs = normalize(mfccs,axis=1)

mfccs = librosa.feature.mfcc(y=y, sr=sample_rate, n_mfcc=12, hop_length=int(sample_rate*0.01), n_fft=int(sample_rate*0.02))
print("mfccs :", mfccs.shape)

plt.figure(figsize=(16,6))
librosa.display.specshow(mfccs,sr=sample_rate, x_axis='time')
plt.show()