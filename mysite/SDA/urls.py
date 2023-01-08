from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main),
    path('add_track', addTrack),
    path('all_track', allTracks),
    path('profile', proFile),
    path('welcome', welcome),
    path('example', example),
    path('login', login),
    path('register', register),
    path('myplaylist', playlist),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
