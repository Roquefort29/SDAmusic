from django import forms
from django.forms import EmailInput, PasswordInput
from .models import *


class TrackForm(forms.ModelForm):
    artist_name = forms.CharField(max_length=100)

    class Meta:
        model = Track
        fields = ['title', 'artist_name', 'genre', 'song', 'photo', 'is_published']

