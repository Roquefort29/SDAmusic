import pymongo
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import *


def main(request):
    return render(request, "../templates/index.html")


def addTrack(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the artist name from the form data
            artist_name = form.cleaned_data['artist_name']

            # Get or create the artist object
            artist, created = Artist.objects.get_or_create(name=artist_name)
            if created:
                artist.bio = ''
                artist.save()

            # Save the track object to the database
            track = form.save(commit=False)
            track.save()

            # Add the artist to the track's many-to-many relationship
            track.artist.add(artist)

            # Save the track again to update the many-to-many relationship
            track.save()
    else:
        form = TrackForm()
    return render(request, '../templates/addTrack.html', {'form': form})


def proFile(request):
    return render(request, "../templates/profile.html")


def albumpage(request):
    return render(request, "../templates/albumpage.html")


def artistpage(request):
    return render(request, "../templates/artistpage.html")


def welcome(request):
    album = Album.objects.all()
    context = {
        'album': album,
    }
    album = Album.objects.all()
    context = {
        'album': album,
    }
    return render(request, "../templates/welcome.html", context=context)


def example(request):
    track = Track.objects.all()
    context = {
        'track': track,
    }

    return render(request, "../templates/example.html", context=context)


def login(request):
    return render(request, "../templates/login.html")


def register(request):
    return render(request, "../templates/register.html")


def playlist(request):
    artist = Artist.objects.all()
    context = {
        'artist': artist,
    }
    return render(request, "../templates/MediaPlaylist.html", context=context)


def rock(request):
    album = Album.objects.filter(genre=3)
    context = {
        'rock': album,
    }
    return render(request, "../templates/rock.html", context=context)


def rap(request):
    album = Album.objects.filter(genre=2)
    context = {
        'rap': album,
    }
    return render(request, "../templates/rap.html", context=context)


def jazz(request):
    album = Album.objects.filter(genre=4)
    context = {
        'jazz': album,
    }
    return render(request, "../templates/jazz.html", context=context)


def phonk(request):
    album = Album.objects.filter(genre=5)
    context = {
        'phonk': album,
    }
    return render(request, "../templates/phonk.html", context=context)


def pop(request):
    album = Album.objects.filter(genre=1)
    context = {
        'pop': album,
    }
    return render(request, "../templates/pop.html", context=context)


def albums(request):
    album = Album.objects.all()
    context = {
        'album': album
    }
    return render(request, "../templates/albums.html", context=context)
