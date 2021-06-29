# photon/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('webcam', views.webcam, name='webcam')

]