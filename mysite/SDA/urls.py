from django.urls import path

from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main),
    path('add_track', addTrack),
    path('profile', proFile),
    path('welcome', welcome),
    path('example', example),
    path('login', login),
    path('register', register),
    path('artists', artists, name="artist_list"),
    path('artist/<slug:slug>/', artist_detail, name='artist_detail'),
    path('rock', rock),
    path('pop', pop),
    path('phonk', phonk),
    path('jazz', jazz),
    path('rap', rap),
    path('albums', albums, name="album_list"),
    path('album/<slug:slug>/', album_detail, name='album_detail')
,
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
