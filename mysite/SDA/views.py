import pymongo
from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def main(request):
    return render(request, "../templates/index.html")


def allTracks(request):
    return render(request, "../templates/allTracks.html")


def addTrack(request):
    return render(request, "../templates/addTrack.html")


def proFile(request):
    return render(request, "../templates/profile.html")


def welcome(request):
    return render(request, "../templates/welcome.html")


def example(request):
    album = Album.objects.all()
    artist = Artist.objects.all()
    context = {
        'album': album,
        'artist': artist
    }

    return render(request, "../templates/example.html", context=context)


def login(request):
    return render(request, "../templates/login.html")
