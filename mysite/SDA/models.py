from djongo import models
#check

class User(models.Model):  # user acc. info
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/', blank=True)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Genre(models.Model):  # genre
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['name']

    def __str__(self):
        return self.name


class Artist(models.Model):  # artist
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/', blank=True)
    is_verify = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'
        ordering = ['name']

    def __str__(self):
        return self.name


class Album(models.Model):  # album
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    title = models.CharField(max_length=150)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, related_name='albumArtist')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='albumGenre')
    photo = models.ImageField(upload_to='photos/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Published?')

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering = ['title']

    def __str__(self):
        return self.title


class Track(models.Model):  # track
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    title = models.CharField(max_length=150)
    duration = models.DurationField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='trackGenre')
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, related_name='trackArtist')
    album = models.ForeignKey(Album, on_delete=models.PROTECT, related_name='trackAlbum')
    photo = models.ImageField(upload_to='photos/', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published?')

    class Meta:
        verbose_name = 'Track'
        verbose_name_plural = 'Songs'
        ordering = ['title']

    def __str__(self):
        return self.title


class Playlist(models.Model):  # playlist
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    title = models.CharField(max_length=150)
    track = models.ForeignKey(Track, on_delete=models.PROTECT, related_name='playlistTrack')
    photo = models.ImageField(upload_to='photos/', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='playlistAuthor')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MyMusics(models.Model):  # Myplaylist
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    title = models.CharField(max_length=150)
    track = models.ForeignKey(Track, on_delete=models.PROTECT, related_name='MyPlaylistTrack')
    photo = models.ImageField(upload_to='photos/', blank=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title