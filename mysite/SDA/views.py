from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    album = Album.objects.all
    context = {
        'slug': album,
        'title': album,
    }
    return render(request,"../templates/index.html",context)