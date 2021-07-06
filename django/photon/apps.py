from django.apps import AppConfig
from tensorflow.keras import models

# project(application)이 처음 시작할 때(장고 서버 시작할때) 각각의 app에 있는 Config 클래스의 객체 생성
# Photon Config -> app에 대한 설정정보를 가지고 있는 클래스
# app이 일하면서 필요한 자원들이 있으면 이 클래스의 instance/class변수로 정의할 수 있음 
class PhotonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photon'
    model = models.load_model(r'model\yolov4')
