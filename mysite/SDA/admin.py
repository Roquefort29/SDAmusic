from django.contrib import admin

from .models import *


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'genre', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'artist')
    list_editable = ('is_published',)
    list_filter = ('artist', 'genre', 'is_published')


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_verify')
    list_editable = ('is_verify',)
    search_fields = ('name',)


class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'album', 'genre', 'is_published')


admin.site.register(User)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Playlist)
