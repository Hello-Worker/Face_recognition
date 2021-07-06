# photon/urls.py
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib import admin

app_name = 'photon'

urlpatterns = [
    path('index', views.index, name='index'),
    path('request', TemplateView.as_view(template_name='photon/request.html'),name='req'),
    path('save', views.save_image, name='save'),
    path('admin/', admin.site.urls)
]