from django.shortcuts import render
from django.http import HttpResponse
import cv2


# Create your views here.
def index(request):
    return render(request, "photon/index.html")

def webcam(request):
    cap = cv2.VideoCapture(0)
    if cap.isOpened() == False:
        print("웹캠 연결 실패")
        exit(1)  
    
    while True:
        ret, img = cap.read()  
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