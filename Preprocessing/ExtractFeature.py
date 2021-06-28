import os
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

def saveNpz(file_num, file_path, category, feature, mfccs, save_path, whatis):
    # make train npz files
    for i in range(0, file_num):
        file = (file_path + category + '/' + str(i) + '.wav')
        # extract feature
        feature = extract_feature(file, FEATURE_LENGTH_TIME)
        mfccs.append(feature)
    # save MFCC features
    np.savez(save_path + category, X = mfccs) 
    print(category + " " + whatis + " done")

file_formats = ['wav/', 'npzs/']
folder_names = ['4_train/', '5_validation/', '6_test/']
file_path = '/Users/m/Desktop/Data/'
categories = ['clover', 'genie', 'news', 'remotecontroller', 'time', 'todayschedule', 'todayweather', 'volumedown', 'volumeup']
train_file_num = 55
val_file_num = 17
test_file_num = 17
FEATURE_LENGTH_TIME = 23

# define file paths
train_file_path = file_path + folder_names[0] + file_formats[0]
val_file_path = file_path + folder_names[1] + file_formats[0]
test_file_path = file_path + folder_names[2] + file_formats[0]
train_save_path = file_path + folder_names[0] + file_formats[1]
val_save_path = file_path + folder_names[1] + file_formats[1]
test_save_path = file_path + folder_names[2] + file_formats[1]

# make directories
for fm in file_formats:
    for fn in folder_names:
        if not os.path.exists(file_path+fn):
            os.mkdir(file_path+fn)
        if not os.path.exists(file_path+fn+fm):
            os.mkdir(file_path+fn+fm)

for category in categories:
    train_feature, val_feature, test_feature = None, None, None
    train_mfccs, val_mfccs, test_mfccs = [], [], []
    
    # make npz files
    saveNpz(train_file_num, train_file_path, category, train_feature, train_mfccs, train_save_path, 'train')
    saveNpz(val_file_num, val_file_path, category, val_feature, val_mfccs, val_save_path, 'val')
    saveNpz(test_file_num, test_file_path, category, test_feature, test_mfccs, test_save_path, 'test')