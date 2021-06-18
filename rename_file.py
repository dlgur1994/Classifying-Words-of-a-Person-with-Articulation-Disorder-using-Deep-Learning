import os

file_path = '/Users/m/Desktop/recordings/separated/soundup'
file_names = os.listdir(file_path)
cnt = 0

for file_name in file_names:
    if file_name == '.DS_Store':
        continue
    # print(file_name)
    src = os.path.join(file_path, file_name)
    dst = str(cnt) + '.wav'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    cnt += 1