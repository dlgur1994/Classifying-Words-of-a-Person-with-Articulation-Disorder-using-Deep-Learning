import numpy as np
import os

train_file_path = '/Users/m/Desktop/Data/4_train/npzs/'
val_file_path = '/Users/m/Desktop/Data/5_validation/npzs/'
test_file_path = '/Users/m/Desktop/Data/6_test/npzs/'
train_save_path = '/Users/m/Desktop/Data/4_train/train_X'
val_save_path = '/Users/m/Desktop/Data/5_validation/val_X'
test_save_path = '/Users/m/Desktop/Data/6_test/test_X'
train_X = []
val_X = []
test_X = []

for f in os.listdir(train_file_path):
    if f == '.DS_Store':
        continue
    data = np.load(train_file_path + f)
    train_X.extend(data['X'])
# save MFCC features
np.savez(train_save_path, X = train_X) 
print("train file done")

for f in os.listdir(val_file_path):
    if f == '.DS_Store':
        continue
    data = np.load(val_file_path + f)
    val_X.extend(data['X'])
# save MFCC features
np.savez(val_save_path, X = val_X) 
print("validation file done")

for f in os.listdir(test_file_path):
    if f == '.DS_Store':
        continue 
    data = np.load(test_file_path + f)
    test_X.extend(data['X'])
# save MFCC features
np.savez(test_save_path, X = test_X) 
print("test file done")