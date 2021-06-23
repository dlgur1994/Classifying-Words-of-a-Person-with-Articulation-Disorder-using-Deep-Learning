import os
import shutil

origin_path = '/Users/m/Desktop/Data/2_separated/'
save_path = '/Users/m/Desktop/Data/3_renamed/'
categories = ['clover', 'genie', 'news', 'remotecontroller', 'time', 'todayschedule', 'todayweather', 'volumedown', 'volumeup']
copy_name = 'cp'

for category in categories:
    os.mkdir(save_path+category)
    cnt = 0
    file_path = origin_path + category
    file_names = os.listdir(file_path)
    
    for file_name in file_names:
        if 'umm' in file_name:
            continue
        if category+'30' in file_name:
            src = os.path.join(file_path, file_name)
            copy = os.path.join(file_path, copy_name)
            shutil.copy(src,copy)
            dst = str(cnt) + '.wav'
            dst = os.path.join(save_path+category, dst)
            os.rename(copy, dst)
            cnt += 1

    for file_name in file_names:
        if 'umm' in file_name:
            continue
        if category+'70' in file_name:
            src = os.path.join(file_path, file_name)
            copy = os.path.join(file_path, copy_name)
            shutil.copy(src,copy)
            dst = str(cnt) + '.wav'
            dst = os.path.join(save_path+category, dst)
            os.rename(copy, dst)
            cnt += 1