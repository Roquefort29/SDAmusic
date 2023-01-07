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
    client = pymongo.MongoClient("mongodb+srv://Syrym:SuperSyr29@sdadb.krcvr71.mongodb.net/?retryWrites=true&w=majority")
    db = client["SDA_music_stream"]
    colle = db["SDA_album"]

    data_from_db = colle.find({})
    return render(request, "../templates/example.html", {"album": data_from_db})


def login(request):
    return render(request, "../templates/login.html")
