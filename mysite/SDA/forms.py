from django import forms
from django.forms import EmailInput, PasswordInput
from .models import *


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['slug', 'title', 'artist', 'album', 'genre', 'song', 'photo', 'is_published']


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['slug', 'name', 'photo']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['slug', 'title', 'artist', 'genre', 'photo', 'is_published']

    tracks = forms.inlineformset_factory(Album, Track, form=TrackForm, extra=1)
