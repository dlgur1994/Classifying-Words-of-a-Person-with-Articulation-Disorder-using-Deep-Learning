import numpy as np

train_save_path = '/Users/m/Desktop/Data/4_train/'
val_save_path = '/Users/m/Desktop/Data/5_validation/'
test_save_path = '/Users/m/Desktop/Data/6_test/'
train_file_num = 55
val_file_num = 17
test_file_num = 17
class_num = 9
train_labels = []
val_labels = []
test_labels = []

for i in range(0, class_num):
    for j in range(0, train_file_num):
        train_labels.append(i)
    for j in range(0, val_file_num):
        val_labels.append(i)
    for j in range(0, test_file_num):
        test_labels.append(i)

np.savez(train_save_path + 'train_y', y = train_labels)
np.savez(val_save_path + 'val_y', y = val_labels)
np.savez(test_save_path + 'test_y', y = test_labels)