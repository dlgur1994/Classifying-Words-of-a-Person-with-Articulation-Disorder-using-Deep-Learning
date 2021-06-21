import os
import shutil

file = 'news'
file_path = '/Users/m/Desktop/recordings/separated/' + file
file_names = os.listdir(file_path)
copy_name = 'cp'
save_path = '/Users/m/Desktop/recordings/final/' + file
cnt = 0

os.mkdir(save_path)

for file_name in file_names:
    if file+'30' in file_name:
        src = os.path.join(file_path, file_name)
        copy = os.path.join(file_path, copy_name)
        shutil.copy(src,copy)
        dst = str(cnt) + '.wav'
        dst = os.path.join(save_path, dst)
        os.rename(copy, dst)
        cnt += 1

for file_name in file_names:
    if file+'70' in file_name:
        src = os.path.join(file_path, file_name)
        copy = os.path.join(file_path, copy_name)
        shutil.copy(src,copy)
        dst = str(cnt) + '.wav'
        dst = os.path.join(save_path, dst)
        os.rename(copy, dst)
        cnt += 1