from django import forms
from django.forms import EmailInput, PasswordInput
from .models import *


class UserRegister(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.CharField(widget=EmailInput)
    password = forms.CharField(widget=PasswordInput)
    confirm_password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ["username", "email", "password", "confirm_password"]
