from django.contrib import admin

from .models import *


class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'artist', 'genre', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'artist')
    list_editable = ('is_published',)
    list_filter = ('artist', 'genre', 'is_published')


class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'is_verify')
    list_editable = ('is_verify',)
    search_fields = ('name',)


class TrackAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'get_artist', 'duration', 'album', 'genre', 'is_published')


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PlaylistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(User)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Images)
