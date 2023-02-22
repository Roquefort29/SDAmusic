from django import forms
from django.forms import EmailInput, PasswordInput
from .models import *


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['slug', 'title', 'artist', 'genre', 'song', 'photo', 'is_published']


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['slug', 'name', 'photo']
