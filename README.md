## 1.	프로젝트 기획 배경
딥러닝을 활용하여 안면 인식 로그인 서비스를 웹페이지에 구현해보고자 하는 목적을 가지고 진행된 프로젝트이다. 코로나19로 인한 마스크 착용이 늘고 있는 요즘 세태에 맞춰 마스크를 벗지 않아도 사용자를 인식할 수 있도록 하며, 사용자가 로그인 시도 시 실시간 캡쳐를 통해 정확도를 예측할 수 있도록 했다. 90% 이상의 정확도를 보일 시 로그인을 허용하도록 구현했으며, 최근 최적의 속도와 높은 정확도를 보이는 Yolov4를 통해 안면인식 로그인 AI를 구축해보았다. 

<img src="https://user-images.githubusercontent.com/75672831/124614729-8364da80-deaf-11eb-80a8-c5bac28bc62b.JPG" width="70%" height="50%" title="px(픽셀) 크기 설정" alt="가상화면"></img>

## 2.	프로젝트 소개<br/>  
<br/>
<img src="https://user-images.githubusercontent.com/75672831/124615900-9c21c000-deb0-11eb-9d23-25e112be380a.JPG" width="50%" height="70%" alt="로그인구현"></img>

1) 웹페이지내 실시간 이미지 캡처를 통한 안면 인식(정면 응시 요망)
2) 사용자 마스크 착용 유무 모두 인식 가능
3) 관리자의 안면 인식을 통한 자동 로그인 서비스
4) 관리자 외 관리자 서비스 사용 불가<br/>  

## 3.	개발환경
CPU i7-1165G7<br/>
RAM 16GB

-Face_recognition<br/>
cmake 3.2<br/>
dlib 19.22<br/>
face_recognition 1.3<br/>
face_recognition_models 0.3<br/>
Opencv 4.5<br/>
Python 3.8<br/>
Tensorflow 2.5<br/>
<br/>
-Inception-resnet v1<br/>
Google Colab<br/>
Linux-5.4.104+-x86_64-with-Ubuntu-18.04-bionic<br/>
Inception-resnet v1<br/>
Keras 2.4<br/>
Matplotlib 3.2<br/>
Numpy 1.19<br/>
PILLOW 7.1<br/>
Python 3.7<br/>
<br/>
-Yolov4<br/>
Google Colab<br/>
Linux-5.4.104+-x86_64-with-Ubuntu-18.04-bionic<br/>
Python 3.7<br/>
CUDA 11.2<br/>
Opencv 3.2<br/>
<br/>  
## 4. 타임라인

![타임라인](https://user-images.githubusercontent.com/75672831/124616639-38e45d80-deb1-11eb-9d41-9ccebbc2c481.JPG)

## 5. 모델 성능 평가

### 1) Face_recognition
- 정확도가 71% 정도로 높지 않았음
- 팀원 4명의 얼굴 이미지를 디렉토리에 넣어 이미지 데이터셋을 만드는 형식으로 추가 학습이 불가

### 2) Inception_resnet_v1
- Val_accuracy, Accuracy 모두 1 도출. 정확도 자체는 높은 편.
- A의 사진들은 다른 사진들에 비해 저화질이었는데, A의 정확도가 낮은 편이었던 것을 미루어 보아 학습시킨 사진의 선명도에 따라 정확도의 퍼센티지가 높고 낮아질 수도 있을 것이다 라는 추측을 할 수 있었음
- 단순 분류모델이기 때문에 헤어스타일, 배경 등에 관계없이 얼굴 인식 시스템을 구현하기 위해 object detection이 가능한 모델로 변경.

### 3) Yolov4
- Object Detection이 가능한 모델 중 SOTA 모델 선정</br>  </br>  


## 6. Yolov4 모델 

![학습과정](https://user-images.githubusercontent.com/75672831/124618573-dd1ad400-deb2-11eb-99a7-f43a553d7ce1.JPG)


### 1) 팀원 4명의 사진 1000장 수집 및 전처리

### 2) Custom Data을 이용해 Transfer Learning 진행
- Google Colab의 GPU 사용
- Yolov4에서 제공하는 Pretrained Weights에 본 조가 준비한 이미지 데이터로 transfer learning 진행(yolov4.conv.137 : 특징 추출에 특화된 가중치를 넣어 학습)

### 3) 학습
- 첫 번째 학습에서는 각자가 직접 찍은 조원 4명의 사진 800장을 약 12시간동안 추가 학습. A와 D의 경우 마스크를 썼을 때와 쓰지 않았을 때 모두 잘 구별해냈으나 B가 마스크를 쓰지 않았을 때와 C가 마스크를 썼을 때의 사진에 대한 정확도가 낮았음
- 두 번째 학습에서는 정확도가 낮은 두 명의 팀원 데이터를 추가 확보 후 재학습: 추가 학습
- 최종적으로 4명의 얼굴을 정확히 인식(정확도 결과 나오면 보완)

### 4) Yolov4를 Tensorflow 모델로 변환
- 추후 Django와의 연동을 용이하게 하기 위해 darknet 모델을 Tensorflow 모델로 변환 후 export
- Tensorflow-yolov4-tflite를 통해 모델을 저장

### 5) Django로 웹페이지 내 안면인식 로그인 서비스 구현
- 메인화면 구축
- 사용자 계정 db 생성
- 로그인 화면 및 폼 활성화
- 웹캠 연동을 통해 실시간 이미지 수집
- ajax로 서버에 이미지 전송
- 모델 연동하여 예측 결과 웹으로 구현
- 예측할 때마다 모델을 불러오는 것이 아니라 서버 최초 실행 시 apps.py에서 모델을 한 번에 불러올 수 있도록 진행


