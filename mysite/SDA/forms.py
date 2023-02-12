from django import forms
from django.forms import EmailInput, PasswordInput
from .models import *


class UserRegister(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Your Username')
    email = forms.CharField(widget=EmailInput)
    password = forms.CharField(widget=PasswordInput())
    confirm_password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ["username", "email", "password", "confirm_password"]

    def clean(self):
        cleaned_data = super(UserRegister, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
