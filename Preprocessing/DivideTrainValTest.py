import os
import shutil

def storeFiles(file_path, file_name, cnt, store_path, category):
    src = os.path.join(file_path, file_name)
    copy = file_path + 'cp.wav'
    shutil.copy(src,copy)
    dst = str(cnt) + '.wav'
    dst = os.path.join(store_path+category, dst)
    os.rename(copy, dst)

origin_file_path = '/Users/m/Desktop/Data/3_renamed/'
train_file_path = '/Users/m/Desktop/Data/4_train/wav/'
val_file_path = '/Users/m/Desktop/Data/5_validation/wav/'
test_file_path = '/Users/m/Desktop/Data/6_test/wav/'
categories = ['clover', 'genie', 'news', 'remotecontroller', 'time', 'todayschedule', 'todayweather', 'volumedown', 'volumeup']

for category in categories:
    cnt = 0
    train_cnt = 0
    val_cnt = 0
    test_cnt = 0
    file_path = origin_file_path + category
    file_names = os.listdir(file_path)

    if not os.path.exists(train_file_path+category):
        os.mkdir(train_file_path+category)
    if not os.path.exists(val_file_path+category):
        os.mkdir(val_file_path+category)
    if not os.path.exists(test_file_path+category):
        os.mkdir(test_file_path+category)
    
    for file_name in file_names:
        if file_name == '.DS_Store':
            continue
        elif (cnt%5 == 0 and cnt<85): # store as a test file
            storeFiles(file_path, file_name, test_cnt, test_file_path, category)
            test_cnt += 1
        elif (cnt%5 == 1 and cnt<85): # store as a validation file
            storeFiles(file_path, file_name, val_cnt, val_file_path, category)  
            val_cnt += 1 
        elif (cnt < 89): # store as a train file 
            storeFiles(file_path, file_name, train_cnt, train_file_path, category)
            train_cnt += 1
        else:
            break
        cnt += 1