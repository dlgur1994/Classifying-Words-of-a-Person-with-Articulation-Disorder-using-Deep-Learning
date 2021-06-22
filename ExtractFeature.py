import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

def extract_feature(file, sec):
    X, sample_rate = librosa.load(file)
    # print('Sampling rate (Hz): %d' %sample_rate)
    # print('Audio length (seconds): %.2f' % (len(X) / sample_rate))
    
    # extract MFCC feature
    # n_fft: the length of a frame, hop_length: gap between two frames 
    mfcc = librosa.feature.mfcc(X, n_mfcc=13, n_fft=int(sample_rate*0.025), hop_length=int(sample_rate*0.01))
    # print(mfcc.shape)
    # print(mfcc)
    
    # adjust input size consistently
    pad2d = lambda a, i: a[:, 0:i] if a.shape[1] > i else np.hstack(a, np.zeros(a.shape[0], i-a.shape[1]))
    mfcc_padded = pad2d(mfcc, 100*sec)
    # plt.figure(figsize=(16,6))
    # librosa.display.specshow(mfcc_padded, sr=sample_rate, x_axis='time')
    # plt.show()
    return mfcc_padded

category_name = 'clover'
origin_file_path = '/Users/m/Desktop/recordings2/separated/'
save_file_path = '/Users/m/Desktop/recordings2/npz/'
n_files = 1
feature_length_time = 1
all_mfccs = []

for i in range(0, n_files):
    all_mfccs = []
    file = (origin_file_path + category_name + '/' + str(i) + '.wav')
    
    # extract feature
    feature = extract_feature(file, feature_length_time)
    all_mfccs.append(feature)

# save MFCC features
np.savez(save_file_path + category_name, X = all_mfccs) 
print(category_name + " done")