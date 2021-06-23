import os
import shutil

origin_file_path = '/Users/m/Desktop/Data/3_renamed/'
train_file_path = '/Users/m/Desktop/Data/4_train/wav/'
test_file_path = '/Users/m/Desktop/Data/5_test/wav/'
categories = ['clover', 'genie', 'news', 'remotecontroller', 'time', 'todayschedule', 'todayweather', 'volumedown', 'volumeup']
copy_name = 'cp'

for category in categories:
    os.mkdir(train_file_path+category)
    os.mkdir(test_file_path+category)
    cnt = 0
    train_cnt = 0
    test_cnt = 0
    file_path = origin_file_path + category
    file_names = os.listdir(file_path)
    
    for file_name in file_names:
        # store as a test file
        if (cnt%5==0 and cnt<85):
            src = os.path.join(file_path, file_name)
            copy = os.path.join(file_path, copy_name)
            shutil.copy(src,copy)
            dst = str(test_cnt) + '.wav'
            dst = os.path.join(test_file_path+category, dst)
            os.rename(copy, dst)
            test_cnt += 1

        # store as a train file    
        elif (cnt<89):
            src = os.path.join(file_path, file_name)
            copy = os.path.join(file_path, copy_name)
            shutil.copy(src,copy)
            dst = str(train_cnt) + '.wav'
            dst = os.path.join(train_file_path+category, dst)
            os.rename(copy, dst)
            train_cnt += 1
        
        else:
            break

        cnt += 1