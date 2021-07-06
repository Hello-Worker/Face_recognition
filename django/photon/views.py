
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt #csrf 적용 안받도록 처리.
from tensorflow.python.ops.gen_control_flow_ops import abort_eager_fallback 
from .apps import PhotonConfig
from PIL import Image
from io import BytesIO
from django.contrib.auth import views, login, get_user_model
from django.contrib.auth.models import User
from django.db import models
import cv2, base64
import numpy as np
import tensorflow as tf


@csrf_exempt

def index(request): # 메인 홈
    return render(request, "photon/index.html")

@csrf_exempt
def save_image(request): #이미지 처리
    global prob_list, label_list 

    if request.method == 'POST':
        # 이미지 오픈
        img_string = request.POST['image'] # 이미지 base64 데이터 받음
        img_str = base64.b64decode(img_string) # base64 데이터 디코딩
        img = Image.open(BytesIO(img_str)).convert('RGB') # 컬러이미지로 반환
        

        # 이미지 변환
        img_resize = img.resize((608,608))  #input shape으로 resize
        arr = np.array(img_resize) # 넘파이 배열로
        arr = arr[np.newaxis, ...]
        arr = arr/255. # 정규화
        IOU_THRESH = 0.5 # 겹칠 때 0.5이상이면 제거
        CONFIDENCE_SCORE_THRESH = 0.3 #0.3보다 낮은 애는 없앤다
        
        # 이미지 예측
        input_tensor = tf.convert_to_tensor(arr) # 텐서타입으로 변환
        pred = PhotonConfig.model.predict(input_tensor) 
        boxes = pred[:,:,0:4] # 박스 좌표
        pred_conf = pred[:,:,4:] # 클래스 확률
    
        boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression( # 박스 겹치기
            boxes = tf.reshape(boxes, (tf.shape(boxes)[0],-1,1,4)), # boexes[0]: 1을 그대로 주고, -1 : 남는 것.->(1,16,1,4)  4차원으로
            scores = tf.reshape(pred_conf, (tf.shape(pred_conf)[0], -1,tf.shape(pred_conf)[-1])),
            max_output_size_per_class = 50, # 클래스 당 비
            max_total_size = 50, # 모든 클래스에서 유지되는 최대 박스 수 
            iou_threshold = IOU_THRESH, 
            score_threshold = CONFIDENCE_SCORE_THRESH) 
        
        scores = scores.numpy() 
        classes = classes.numpy()
        scores_max = np.max(scores, axis=-1)*100 # 확률 최대 값
        label_list = int(classes[0][0]) 

        label_map = ['Song','Kang','Kwon','Chae'] # 클래스 이름 설정
        label_list = label_map[label_list]
        prob_list= int(scores_max)
        user_id = User.objects.get(username=label_list, is_superuser=True) #동일한 이름의 username조회
        if int(prob_list) > 90: # 90 이상 시 로그인
            login(request, user_id)
            dic = {
                'label_list':label_list,
                "prob_list":prob_list
            }
        
        return JsonResponse(dic, status=200) # 바이너리로 변환하려 보냄 request로

    
