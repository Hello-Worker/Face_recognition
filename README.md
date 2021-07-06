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

#### -Face_recognition<br/>
cmake 3.2<br/>
dlib 19.22<br/>
face_recognition 1.3<br/>
face_recognition_models 0.3<br/>
Opencv 4.5<br/>
Python 3.8<br/>
Tensorflow 2.5<br/>
<br/>
#### -Inception-resnet v1<br/>
Google Colab<br/>
Linux-5.4.104+-x86_64-with-Ubuntu-18.04-bionic<br/>
Inception-resnet v1<br/>
Keras 2.4<br/>
Matplotlib 3.2<br/>
Numpy 1.19<br/>
PILLOW 7.1<br/>
Python 3.7<br/>
<br/>
#### -Yolov4<br/>
Google Colab<br/>
Linux-5.4.104+-x86_64-with-Ubuntu-18.04-bionic<br/>
Python 3.7<br/>
CUDA 11.2<br/>
Opencv 3.2<br/>
<br/>  
## 4. 타임라인

![타임라인](https://user-images.githubusercontent.com/75672831/124616639-38e45d80-deb1-11eb-9d41-9ccebbc2c481.JPG)

## 5. 모델 성능 평가 및 선정 

![KakaoTalk_20210706_235841147](https://user-images.githubusercontent.com/75672831/124629268-3d624380-debc-11eb-80b6-e353cf81a535.png)

#### <모델 선택 기준><br/>
A. Custom data 학습 가능한가?<br/>
B. Object detection 가능한가?<br/>
C. 평가 정확도가 높고, 예측 속도가 빠른 모델인가?<br/>

1) Face_recognition(B만족 / A,C 불만족)
- 정확도: 71% => 타모델보다 낮은 정확도.
- 추가학습, 모델 개선 불가

2) Inception_resnet_v1(A,C만족 / B 불만족)
- Val_accuracy, Accuracy : 1  => 높은 정확도.
- 학습데이터 Aset의 정확도 낮음 => A의 dataset이 저화질인 것이 원인으로 추측됨.
- 단순 분류모델. Object dection불가능.
(헤어스타일, 배경 등에 관계없이 얼굴 인식 시스템을 구현하기 위해 object detection이 가능한 모델 필요)
.
3) Yolov4(A,B,C만족)
- Object Detection이 가능한 모델 중 SOTA 모델 선정



## 6. Yolov4 모델 

<img src="https://user-images.githubusercontent.com/75672831/124629146-23286580-debc-11eb-937d-199d9fadc4a6.JPG" width="50%" height="50%" alt="yolov4"></img>

![학습과정](https://user-images.githubusercontent.com/75672831/124618573-dd1ad400-deb2-11eb-99a7-f43a553d7ce1.JPG)


#### 1) 팀원 4명의 사진 1000장 수집 및 전처리
##### <Custom Data 직접 생성>
- 팀원 4명의 마스크 착용 사진, 미착용 사진 각 100장(총 800장)
- 첫 학습 후 팀원 2명의 인식률이 낮아 팀원 1명의 마스크 미착용 사진 100장, 착용 사진 100장(총 200장) 추가 
=> 도합 1000장의 마스크 착용 사진, 미착용 사진 사용
##### <데이터 전처리>
- labelimg를 이용해 모든 사진의 얼굴에 라벨링 진행(이마 중간부터 턱 끝까지)
- Label Annotation 파일들을 yolo 형식 txt로 변환

#### 2) Custom Data을 이용해 Transfer Learning 진행
- Google Colab의 GPU 사용
- Yolov4에서 제공하는 Pretrained Weights에 본 조가 준비한 이미지 데이터로 transfer learning 진행(yolov4.conv.137 : 특징 추출에 특화된 가중치를 넣어 학습)

#### 3) 학습
- 첫 번째 학습에서는 각자가 직접 찍은 조원 4명의 사진 800장을 약 12시간동안 추가 학습. A와 D의 경우 마스크를 썼을 때와 쓰지 않았을 때 모두 잘 구별해냈으나 B가 마스크를 쓰지 않았을 때와 C가 마스크를 썼을 때의 사진에 대한 정확도가 낮았음
- 두 번째 학습에서는 정확도가 낮은 두 명의 팀원 데이터를 추가 확보 후 재학습: 추가 학습
- 최종적으로 4명의 얼굴을 정확히 인식(정확도 결과 나오면 보완)

#### 4) Yolov4를 Tensorflow 모델로 변환
- 추후 Django와의 연동을 용이하게 하기 위해 darknet 모델을 Tensorflow 모델로 변환 후 export
- Tensorflow-yolov4-tflite를 통해 모델을 저장

#### 5) Django로 웹페이지 내 안면인식 로그인 서비스 구현
- 메인화면 구축
- 사용자 계정 db 생성
- 로그인 화면 및 폼 활성화
- 웹캠 연동을 통해 실시간 이미지 수집
- ajax로 서버에 이미지 전송
- 모델 연동하여 예측 결과 웹으로 구현
- 예측할 때마다 모델을 불러오는 것이 아니라 서버 최초 실행 시 apps.py에서 모델을 한 번에 불러올 수 있도록 진행<br/><br/>

## 7.  웹페이지 구축(인터페이스) : Django, Javascript, HTML5

#### 1) Django 가상 환경 설정
![241](https://user-images.githubusercontent.com/75672831/124625920-2f5ef380-deb9-11eb-8636-6823f04299f9.JPG)

#### 2) Django 프로그램 설치
![46223](https://user-images.githubusercontent.com/75672831/124625964-3ab21f00-deb9-11eb-90b1-7a3f89583fad.JPG)

#### 3) 메인화면 구축(템플릿 참고 https://html5up.net/photon)

- index.html: 메인 화면
- 
<img src="https://user-images.githubusercontent.com/75672831/124626684-dcd20700-deb9-11eb-8f33-23908ee2f987.JPG" width="80%" height="50%"></img>
<img src="https://user-images.githubusercontent.com/75672831/124631083-fffeb580-debd-11eb-915b-99ae06d32244.JPG" width="80%" height="50%"></img>


- login_form: 로그인 화면

<img src="https://user-images.githubusercontent.com/75672831/124626700-dfccf780-deb9-11eb-8e1b-f4eb54dc51ca.JPG" width="80%" height="50%"></img>



## 8. 웹페이지 모델 연동

#### 1) 웹캠 연동하여 실시간 이미지 수집

- request.html: 웹캠 연동, 실시간 이미지 수집, 예측 결과 화면 구현
- Video, Canvas 활용

#### 2) ajax로 수집된 이미지 서버로 전송
#### 3) 모델연동 및 예측 결과 웹으로 전송
#### 4) 웹에서 안면인식 로그인 서비스 구현<br/>

![35235](https://user-images.githubusercontent.com/75672831/124630377-55869280-debd-11eb-90ee-8bad1e4da9a3.JPG)







## 8. 한계 및 개선사항

1) 간혹 타인이 인식되는 경우가 발생. 이는 데이터셋의 절대적인 양 부족 탓으로 생각되며 추후에 추가 학습으로 보완할 수 있을 것으로 보임.
2) 동양인의 경우 서양인에 비해 이목구비가 비교적 덜 뚜렷해 인식률이 낮은 부분도 고려할 수 있었음 -> 추후 동양인의 얼굴이 많이 학습된 모델을 사용하면 정확도 보완 가능 예상
3) 총 세 번의 학습을 진행하였는데, 가장 첫 번째 학습에서는 임의의 기준으로 선정된 연예인 네 명의 800장의 사진을 약 9시간 동안 학습시켰으나 학습 후 테스트 결과 연예인 4명을 모두 맞추지 못해, detection 대상을 연예인에서 조원 4명으로 변경. 연예인 사진으로 진행 시 마스크 합성 및 이미지 수집에 따른 시간 소요가 크게 예상되어 데이터셋 확보의 어려움을 고려해 팀원 4명을 인식하는 것으로 변경.


## 9. 구현시 유의사항

- yolov4 model 구글 드라이브 링크: https://drive.google.com/drive/folders/1Um-007VdjAEXjdK2uw6GjuvqiFw7QX7n?usp=sharing
- Image dataset은 미업로드. 라벨링된 dataset을 경로를 맞춰 디렉토리에 넣고 사용할 수 있음


## 10. 참고 문헌

#### - 템플릿
https://html5up.net/photon

#### - 모델 관련
https://bblib.net/entry/convert-voc-to-yolo-xml-to-yolo-xml-to-txt
https://ukayzm.github.io/python-face-recognition/
https://blog.naver.com/newton89/221794524792
https://github.com/theAIGuysCode/tensorflow-yolov4-tflite
https://jjeamin.github.io/darknet_book/part1_paper/yolov4.html

