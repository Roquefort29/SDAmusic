from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def main(request):
    album = Album.objects.all
    context = {
        'slug': album,
        'title': album,
        'artist': album,
        'image': album,
    }
    return render(request, "../templates/index.html", context)


def allTracks(request):
    return render(request, "../templates/allTracks.html")


def addTrack(request):
    return render(request, "../templates/addTrack.html")


def proFile(request):
    return render(request, "../templates/profile.html")


def welcome(request):
    return render(request, "../templates/welcome.html")
