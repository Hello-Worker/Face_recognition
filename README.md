## 1.	프로젝트 기획 배경
딥러닝을 활용하여 안면 인식 로그인 서비스를 웹페이지에 구현해보고자 하는 목적을 가지고 진행된 프로젝트이다. 코로나19로 인한 마스크 착용이 늘고 있는 요즘 세태에 맞춰 마스크를 벗지 않아도 사용자를 인식할 수 있도록 하며, 사용자가 로그인 시도 시 실시간 캡쳐를 통해 정확도를 예측할 수 있도록 했다. 90% 이상의 정확도를 보일 시 로그인을 허용하도록 구현했으며, 최근 최적의 속도와 높은 정확도를 보이는 Yolov4를 통해 안면인식 로그인 AI를 구축해보았다. 

<img src="https://user-images.githubusercontent.com/75672831/124614729-8364da80-deaf-11eb-80a8-c5bac28bc62b.JPG" width="70%" height="50%" title="px(픽셀) 크기 설정" alt="가상화면"></img>

## 2.	프로젝트 소개<br/>  
<br/>
<img src="https://user-images.githubusercontent.com/75672831/124615900-9c21c000-deb0-11eb-9d23-25e112be380a.JPG" width="50%" height="70%" alt="로그인구현"></img>

1) 실시간 이미지 캡처를 통한 안면 인식(정면 응시 요망)
2) 사용자 마스크 착용 유무 모두 인식 가능
3) 관리자의 안면 인식을 통한 자동 로그인 서비스
4) 관리자 외 관리자 서비스 사용 불가
<br/>
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
