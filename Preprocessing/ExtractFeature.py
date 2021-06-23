import numpy as np
import librosa
from sklearn.preprocessing import minmax_scale
# import librosa.display
# import matplotlib.pyplot as plt

def pad2d(features, fixed_length, padding_value=0):
    rows = []
    for feature in features:
        rows.append(np.pad(feature, (0, fixed_length), 'constant', constant_values=padding_value)[:fixed_length])
    return np.concatenate(rows, axis=0).reshape(-1, fixed_length)

def extract_feature(file, sec):
    X, sample_rate = librosa.load(file)
    # print('Sampling rate (Hz): %d' %sample_rate)
    # print('Audio length (seconds): %.2f' % (len(X) / sample_rate))
    
    # extract MFCC feature
    # n_mfcc=13: features are usually used for speech recognition
    # n_fft: the length of a frame, hop_length: gap between two frames 
    mfcc = librosa.feature.mfcc(X, n_mfcc=13, n_fft=int(sample_rate*0.025), hop_length=int(sample_rate*0.01))

    # normalize MFCC features
    mfcc_normalized = minmax_scale(mfcc, axis=0, copy=True)
    
    # adjust input size consistently
    mfcc_padded = pad2d(mfcc_normalized, 100*sec)
    
    # plt.figure(figsize=(16,6))
    # librosa.display.specshow(mfcc_padded, sr=sample_rate, x_axis='time')
    # plt.show()
    return mfcc_padded

train_file_path = '/Users/m/Desktop/Data/4_train/wav/'
test_file_path = '/Users/m/Desktop/Data/5_test/wav/'
train_save_path = '/Users/m/Desktop/Data/4_train/npzs/'
test_save_path = '/Users/m/Desktop/Data/5_test/npzs/'
categories = ['clover', 'genie', 'news', 'remotecontroller', 'time', 'todayschedule', 'todayweather', 'volumedown', 'volumeup']
train_file_num = 72
test_file_num = 17
feature_length_time = 23

for category in categories:
    train_feature = None
    test_feature = None
    train_mfccs = []
    test_mfccs = []

    # make train npz files
    for i in range(0, train_file_num):
        train_file = (train_file_path + category + '/' + str(i) + '.wav')
        # extract feature
        train_feature = extract_feature(train_file, feature_length_time)
        train_mfccs.append(train_feature)
    # save MFCC features
    np.savez(train_save_path + category, X = train_mfccs) 
    print(category + " train done")

    # make test npz files
    for i in range(0, test_file_num):
        test_file = (test_file_path + category + '/' + str(i) + '.wav')
        # extract feature
        test_feature = extract_feature(test_file, feature_length_time)
        test_mfccs.append(test_feature)
    # save MFCC features
    np.savez(test_save_path + category, X = test_mfccs) 
    print(category + " test done")