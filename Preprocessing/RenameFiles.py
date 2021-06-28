import os
import shutil

def doRename(file_path, file_name, cnt, save_path, category):
    src = os.path.join(file_path, file_name)
    copy = file_path + 'cp.wav'
    shutil.copy(src,copy)
    dst = str(cnt) + '.wav'
    dst = os.path.join(save_path+category, dst)
    os.rename(copy, dst)

origin_path = '/Users/m/Desktop/Data/2_separated/'
save_path = '/Users/m/Desktop/Data/3_renamed/'
categories = ['clover', 'genie', 'news', 'remotecontroller', 'time', 'todayschedule', 'todayweather', 'volumedown', 'volumeup']

if not os.path.exists(save_path):
    os.mkdir(save_path)

for category in categories:
    cnt = 0
    file_path = origin_path + category
    file_names = os.listdir(file_path)

    if not os.path.exists(save_path+category):
        os.mkdir(save_path+category)
    
    for file_name in file_names:
        if 'umm' in file_name:
            continue
        if category+'30' in file_name:
            doRename(file_path, file_name, cnt, save_path, category)
            cnt += 1

    for file_name in file_names:
        if 'umm' in file_name:
            continue
        if category+'70' in file_name:
            doRename(file_path, file_name, cnt, save_path, category)
            cnt += 1