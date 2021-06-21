# Classifying Words of a Person with Articulation Disorder

(New Version In Progress)

1. Data
- 9 words
    - 뉴스(news), 리모컨(remote controller), 소리크게(volume up), 소리작게(volume down), 시간(time), 오늘일정(today schedule), 오늘날씨(today weather), 지니야(genie), 클로바(clova)
- Train / Test = 72:18 = 0.8:0.2

2. Data Preprocessing</br>
|Data|Format|Audio Channel|Sample Rate|Bit per Sample|Encoding|
|---|---|---|---|---|---|
|raw|mp4|mono|44.1 kHz|16 bit||
|to_wav|wav|mono|44.1 kHz|16 bit|pcm|
|separated|wav|mono|44.1 kHz|16 bit|pcm|

- why wav? 
    - The wav format is uncompressed, being an exact copy of t he source audio
- extract features
    - use MFCC
    - store features into a npz file

3. Train

4. Test

5. Results