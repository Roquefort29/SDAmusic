import pymongo
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

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
    if request.method == 'POST':
        user_register = UserRegister(request.POST)
        if user_register.is_valid():
            user_register.save()
            messages.success("Зареган братишка")
            return redirect('login')
        else:
            messages.error("Опаньки, не так все просто")
    else:
        user_register = UserRegister()
    return render(request, "../templates/register.html", {"form": user_register})


def playlist(request):
    return render(request, "../templates/MediaPlaylist.html")
