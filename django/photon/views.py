from django.shortcuts import render
from django.http import HttpResponse
import cv2, sys, os, time, uuid


# Create your views here.
def index(request):
    return render(request, "photon/index.html")

def webcam(request):
    IMAGE_DIR = 'images'
    if not os.path.isdir(IMAGE_DIR):
        os.mkdir(IMAGE_DIR)

    labels = ['admin']
    n_images = 10 # 카테고리별로 몇장 씩 만들자
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('웹캠 연결 실패')
        sys.exit(1) # 종료
        
    # 웹캠 이미지 사이즈 설정
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    break_all = False #중복 반복문의 전체를 빠져나오기 위한 bool 변수

    # Label 별로 반복해서 캡쳐
    for label in labels:
        print(f"{label} 라벨 캡쳐")
        time.sleep(2) # 2초 대기.(준비시간)
        
        # 이미지 n_images 개수만큼 캡쳐
        # 한번 반복할때 마다 한장씩 캡쳐.
        for img_num in range(n_images):
            ret, frame= cap.read() # 캡쳐: 성공 여부, 캡쳐 이미지(ndarray) 반환
            
            frame = cv2.flip(frame, 1)
            filename = "{}-{}.jpg".format(label, str(uuid.uuid1()))
            file_path = os.path.join(IMAGE_DIR, filename)
            #화면에 출력
            cv2.imshow('frame', frame)
            #캡처 이미지를 파일로 저장
            cv2.imwrite(file_path, frame)
            print(f"{img_num}번쨰, ", end=" ")
            if cv2.waitKey(1000) == 27: # 27:esc를 누르면 강제 종료. waitkey(2000=>2초) 2초 후에 다음 동작을 캡쳐
                print('강제종료')
                break_all = True
                break
            if break_all: # 반복문 전체를 빠져나오도록 설정.
                break
                
    # 종료: 카메라, 출력창을 종료
    cap.release()
    cv2.destroyAllWindows()