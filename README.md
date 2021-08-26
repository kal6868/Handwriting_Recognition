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
어느정도 예측에는 성공했지만 인식률이 크게 떨어지는 모습을 보여준다. 





