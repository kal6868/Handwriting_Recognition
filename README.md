# 한글 손글씨 인식

폰트체가 아닌 사람을 손글씨를 인공지능으로 학습시켜 실생활에서 적은 손글씨를 얼마나 잘 인식하는지 확인해보고자 하였다.

## Dataset
* Ai HUB 한국어 글자체 이미지(https://aihub.or.kr/aidata/133)
![1  한국어 글자체 이미지](https://user-images.githubusercontent.com/89456014/130992617-30cbdd08-d5a2-42b1-a778-b589d4640566.PNG)   
![그림1](https://user-images.githubusercontent.com/89456014/130998152-f35d924b-3925-415a-86a0-55bb3f701026.png)   


AI Hub에서 제공하는 '한국어 글자체 이미지' 데이터셋에서 '01_handwriting_syllable_images.zip', '02_handwriting_syllable_images.zip',    '01_printed_syllable_images.zip' 3종의 데이터를 사용하였고, 모든 받침의 조합을 사용할 수는 없어 완성형 한글 2350자만 추려내서 각 28,352, 124,120, 112,002개 데이터를 사용하였다.
***
* Text Recognition Data Generator(https://github.com/Belval/TextRecognitionDataGenerator)
![2  TextImageGenerator](https://user-images.githubusercontent.com/89456014/130993927-77968b80-44a9-42a1-b772-def8ac37c748.PNG)   
![3  TextRecognitionDataGenerator](https://user-images.githubusercontent.com/89456014/130998679-24f34db4-6317-45e8-ba7b-69810a9e8f7d.PNG)   
Text Recognition Data Generator를 이용하여 네이버 클로바(https://clova.ai/handwriting)의 손글씨 폰트를 이용하여 글자 데이터 100,000개를 추가로 생성하였다.   

## Train
기존 CNN 모델을 적용하여 학습을 진행시 손실율이 너무 높고, 정확도가 굉장히 낮은 일정 수준이상으로 상승되지 않았다.  

![text-recognition-benchmark](https://user-images.githubusercontent.com/89456014/131002044-e857e788-0436-4ec8-b8e7-70e12fd27b01.png)
그래서, 구글링을 통해 clovaai의 deep-text-recognition-benchmark(https://github.com/clovaai/deep-text-recognition-benchmark) 의 VGG_Extractor 모델을 이용하여 학습을 진행시켰다.

## Recognition
![step14](https://user-images.githubusercontent.com/89456014/131004861-01798a0b-13ba-43de-860e-a620259346e7.png)  
![step57](https://user-images.githubusercontent.com/89456014/131004963-8f4bbd10-e8de-4983-9ac1-501a797647c8.png)  
OpenCV를 이용해서 직접 작성한 손 글씨에 몇가지 처리를 거쳐 글자의 위치만 식별한 뒤, 문장을 글자별로 자른다.  
각 글자를 인공지능을 훈련시켜 얻은 모델에 대입하여 예측 결과를 도출한다.

## Result  
![result](https://user-images.githubusercontent.com/89456014/131006060-f6952d9b-8ddc-4aa8-ad8c-ae6ae21fc01b.png)  
어느정도 예측에는 성공했지만 인식률이 낮은 모습을 보여준다.
인식률이 크게 낮은 이유가 글자별 사각형의 크기가 서로 제각각이여서 훈련데이터 사진 크기로 Resize를 할 때 글자의 모습이 뒤틀려서 훈련 데이터와 비교 후 판별을 할 때 어려움이 있는 것으로 판단했다.

## Alternative

다른 사용자들의 Github를 참고시 사진 크기를 먼저 설정해주면 인식율이 올라가는 것을 발견하여 Streamlit을 이용하여 이를 웹 상에 올려 마우스나 Ipad 같은 입력 기기를 이용해서 직접 글씨를 써보기로 했다.

*참고자료  
https://www.youtube.com/watch?v=JLVB8ZUPojw  
https://github.com/junstar92/hangul-syllable-recognition

![방탄소년단](https://user-images.githubusercontent.com/89456014/131635681-0c4b3ffd-4250-486e-9b6c-4c7258ead5d7.PNG)  

일정한 크기의 네모칸에 한글자씩 써 넣어서 가장 확률이 높은 단어가 채택될 수 있게 하였으며, 각 단어만 인식하는 것은 크게 활용도가 떨어질 것으로 판단하여  
여러개의 글자를 입력하면 하나의 글자가 될 수 있도록 만들었다.  

해당 사진은 '방', '탄', '소', '년', '단' 이라는 글자를 하나씩 인식시켜 '방탄소년단' 이 될 수 있도록 하나의 단어로 합친 모습니다. 


