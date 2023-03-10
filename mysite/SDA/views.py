import pymongo
from django.views.generic import DetailView, ListView

from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from .models import *


def main(request):
    return render(request, "../templates/index.html")


def CreateAlbum(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, '../templates/createAlbum.html', {'form': form})


def addArtist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artist_list')
    else:
        form = ArtistForm()
    return render(request, '../templates/addArtist.html', {'form': form})


def addTrack(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            track = form.save(commit=False)
            track.save()
    else:
        form = TrackForm()
    return render(request, '../templates/addTrack.html', {'form': form})


def addContent(request):
    return render(request, '../templates/addContent.html')


def proFile(request):
    return render(request, "../templates/profile.html")


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


def artists(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists,
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


def album_detail(request, slug):
    album = Album.objects.get(slug=slug)
    id_of_album = album.id
    track = Track.objects.filter(album=id_of_album)
    context = {
        'album': album,
        'track': track,
    }
    return render(request, "../templates/albumpage.html", context=context)


def albums(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }
    return render(request, "../templates/albums.html", context=context)


def artist_detail(request, slug):
    artist = Artist.objects.get(slug=slug)
    id_of_artist = artist.id
    album = Album.objects.filter(artist=id_of_artist)
    context = {
        'artist': artist,
        'album': album,
    }
    return render(request, "../templates/artistpage.html", context=context)

def track_detail(request, slug):
    track = Track.objects.get(slug=slug)
    context = {
        'track': track
    }
    return render(request, "../templates/trackpage.html", context=context)