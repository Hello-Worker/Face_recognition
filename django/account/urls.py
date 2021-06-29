#account/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'account'
urlpatterns = [
    path("login", LoginView.as_view(template_name='account/login_form.html'), name='login'),
]