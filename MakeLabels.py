import numpy as np

file_num = 90
class_num = 9
labels = []
save_path = '/Users/m/Desktop/recordings2/train/y/'

for i in range(0, class_num):
    for j in range(0, file_num):
        labels.append(i)

np.savez(save_path + 'labels', labels)