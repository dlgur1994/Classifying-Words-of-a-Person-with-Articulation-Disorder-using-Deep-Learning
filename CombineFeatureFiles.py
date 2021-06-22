import numpy as np

mfccs = []

train_num = 72
file_path = '/Users/m/Desktop/recordings2/train/'
category_name = 'clover'

N = 39

for i in range(train_num):
    
    
    filename = (file_path + category_name + '/' + i + '.npz')
    f = np.load(filename, 'r')
    print('%d file'%i)
    num = f['X'].shape[0]

    for m in range(num):
        line = f['X'][m]
        narr = []
        for j in range(N):
            s_n = str(line[j]).split()
            s_n[0] = s_n[len(s_n)-1][:-1]
            for numb in s_n:
                if numb == '':
                    continue
                narr.append(float(numb))
            tc.append(narr)
        f.close

tc = np.array(tc)
tc = tc.astype(np.float32)
f.close()

np.savez('desktop/mfcc_train_final/train_data', X = tc)
#전체 set을 합친 npz 파일 저장