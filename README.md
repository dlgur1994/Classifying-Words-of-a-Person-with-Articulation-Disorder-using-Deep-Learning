# Classifying Words of a Person with Articulation Disorder

(New Version In Progress)

1. Data
- 9 words
    - 뉴스(news), 리모컨(remote controller), 소리크게(volume up), 소리작게(volume down), 시간(time), 오늘일정(today schedule), 오늘날씨(today weather), 지니야(genie), 클로바(clova)
- why wav format? 
    - The wav format is uncompressed, being an exact copy of the source audio
- Train / Test = 72:18 = 0.8:0.2

2. Data Preprocessing
- change files
    - raw -> to_wav -> separated
        - clover70.m4a -> clover70.wav: online converter(https://convertio.co/m4a-wav/)
        - clover70.wav -> clover_0.wav ~ clover_69.wav: cut them one by one with 'WavePad'
    > |Data|Format|Audio Channel|Sample Rate|Bit per Sample|Encoding|
    > |---|---|---|---|---|---|
    > |raw|m4a|mono|44.1 kHz|16 bit|.|
    > |to_wav|wav|mono|44.1 kHz|16 bit|pcm|
    > |separated|wav|mono|44.1 kHz|16 bit|pcm|
- extract features
    - ExtractFeature.py
    - extract MFCC
        - n_mfcc = 13 -> for speech recognition, 13 mfcc features are usually used
    - make the length of input same
    - store features into a npz file

3. Train

4. Test

5. Results