from .models import Album


def get_album_songs_count(album: Album) -> int:
    return album.songs.count()


def get_total_songs_duration(album: Album) -> int:
    arr = [item.duration for item in album.songs.all()]
    return sum(arr)
