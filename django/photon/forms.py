# api/forms.py
from django import forms

class UploadForm(forms.Form):
    # from field들을 class 변수로 작성. 변수 이름(요청파라미터 이름) = 요청 파라미터 타입에 맞는 FormField
    upimg = forms.ImageField()

