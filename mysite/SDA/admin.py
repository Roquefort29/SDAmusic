from django.contrib import admin

from .models import *


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'artist')


class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'album', 'genre', 'is_published')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Track, TrackAdmin)
admin.site.register(Playlist)