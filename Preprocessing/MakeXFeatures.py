import numpy as np
import os

def makeOne(file_path, Xs, save_path, whatis):
    for f in os.listdir(file_path):
        if f == '.DS_Store':
            continue
        data = np.load(file_path + f)
        Xs.extend(data['X'])
    # save MFCC features
    np.savez(save_path, X = Xs)
    print(whatis + " file done")

train_file_path = '/Users/m/Desktop/Data/4_train/npzs/'
val_file_path = '/Users/m/Desktop/Data/5_validation/npzs/'
test_file_path = '/Users/m/Desktop/Data/6_test/npzs/'
train_save_path = '/Users/m/Desktop/Data/4_train/train_X'
val_save_path = '/Users/m/Desktop/Data/5_validation/val_X'
test_save_path = '/Users/m/Desktop/Data/6_test/test_X'
train_X, val_X, test_X = [], [], []

makeOne(train_file_path, train_X, train_save_path, 'train')
makeOne(val_file_path, val_X, val_save_path, 'validation')
makeOne(test_file_path, test_X, test_save_path, 'test')