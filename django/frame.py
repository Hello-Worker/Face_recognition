#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

# VideoCapture(정수): 웹캠 연동
def webcam():
    cap = cv2.VideoCapture(0)
# 연동 성공여부
    if cap.isOpened() == False:
        print("웹캠 연결 실패")
        exit(1)  # 프로그램 실행 종료. 1: 비정상 종료
    
    while True:
        # 웹캠으로부터 영상 이미지(Frame) 읽기
        ret, img = cap.read()  # ret: boolean, img: ndarray - 이미지
        if not ret:
            print("이미지 캡처 실패")
            break
        # 캡쳐한 이미지를 화면에 출력
        img = cv2.flip(img, 1)  # 양수: 수평반전, 0: 수직반전, 음수: 수평+수직반전
        cv2.imshow("Frame", img)
        
        if cv2.waitKey(1) == ord('q'):  # q를 입력받으면 웹캠 이미지 읽기(capture) 종료
            break

    # 웹캠 연결 종료        
    cap.release()
    # 출력창 종료
    cv2.destroyAllWindows()






# In[ ]:




