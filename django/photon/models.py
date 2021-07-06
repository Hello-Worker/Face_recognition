# Create your models here.
from django.db import models
from django.contrib.auth import views, login, get_user_model
class User(models.Model):
    user_id = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)