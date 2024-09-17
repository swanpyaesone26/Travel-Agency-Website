from django import forms
from .models import UserRegisterInfo

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserRegisterInfo
        fields = ['username', 'nrc_number', 'phone_number', 'address']

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    nrc_number = forms.CharField(max_length=50)

